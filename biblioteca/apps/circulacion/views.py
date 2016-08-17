from django.shortcuts import redirect
from django.views.generic import TemplateView, View, RedirectView
from django.views.generic.edit import FormView, FormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin

from django.core.urlresolvers import reverse_lazy

# local model import
from apps.lector.models import Lector,TipoLector
from apps.circulacion.models import Ejemplar
from .models import Prestamo, Devolucion

# Local Import
from .functions import generar_pdf
from .forms import LectorPrestamoForm, LibroPrestamoForm, DevolucionForm,DeudoresForm
from datetime import date, datetime, timedelta

from django.db.models import Q


class LectorPrestamoView(FormView):
    template_name = 'circulacion/prestamo/prestamo.html'
    print 'Sali a prestamo'
    form_class = LectorPrestamoForm
    # success_url = reverse_lazy('users_app:login')
    def get_success_url(self):
        return reverse_lazy('users_app:login')

    def form_valid(self, form):
        codigo = form.cleaned_data['lector']
        lector = Lector.objects.get(codigo=codigo)
        return redirect('circulacion_app:ejemplarPrestamo', pk=lector.pk)


class EjemplarPrestamoView(FormMixin, DetailView):
    '''
    Relizacion del prestamos si por dia
    '''
    model = Lector
    template_name = 'circulacion/prestamo/ejemplar.html'
    form_class = LibroPrestamoForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(EjemplarPrestamoView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        # recuperamos el lector y verificamos los libros que tienen prestado
        lector = self.object
        context['prestamos'] = Prestamo.objects.filter(
            lector=lector,
            ejemplar__prestado=True,
            devuelto=False
        )
        context['cantidad'] = context['prestamos'].count()
        return  context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        bibliotecario = self.request.user
        lector = self.object

        # Cantidad de prestamos
        cantidad = Prestamo.objects.filter(lector=lector, devuelto=False).count()
        # recuperar codigo del libro
        codigo = form.cleaned_data["codigo"]

        if cantidad != 0:
            return redirect('circulacion_app:confirmarPrestamo', pk=lector.pk, codigo=codigo)
        else:
            # recuperarmos el ajemplar
            ejemplar = Ejemplar.objects.get(codigo_barras=codigo)
            # recuepramos la fecha de hoy
            hoy = datetime.now()
            dia = hoy.isoweekday()

            if dia == 5:
                # si es viernes se suma 3 dias al la fecha de entrega
                fecha_entrega = hoy + timedelta(days=3)
            else:
                # si el dia es distinto de viernes sol ose suma 1 dia
                fecha_entrega = hoy + timedelta(days=1)

            # Guardamos el prestamo
            prestamo = Prestamo(
                bibliotecario=bibliotecario,
                lector=lector,
                ejemplar=ejemplar,
                fecha_entrega=fecha_entrega
            )
            prestamo.save()

            # ponemos el libro como Prestado y guardamos
            ejemplar.prestado = True
            ejemplar.save()

            return redirect('circulacion_app:printVoucher', pk=prestamo.pk)



class ConfirmarPrestamoView(DetailView):
    '''
    Confirmar el prestamos si el lector tiene mas de dos prestamos
    '''
    model = Lector
    template_name = 'circulacion/prestamo/confirmacion.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmarPrestamoView, self).get_context_data(**kwargs)
        # recuperamos el lector y verificamos los libros que tienen prestado
        lector = self.object
        codigo_barras = self.kwargs.get("codigo")
        context['ejemplar'] = Ejemplar.objects.get(codigo_barras=codigo_barras)
        context['prestamos'] = Prestamo.objects.filter(
            lector=lector,
            ejemplar__prestado=True
        )
        context['cantidad'] = context['prestamos'].count()
        return  context


class RegistrarPrestamoView(View):

    def get(self, request, *args, **kwargs):
        print 'entre a redirectview'
        print self.args
        print self.kwargs
        bibliotecario = self.request.user
        lector = Lector.objects.get(pk=self.kwargs.get('pk'))
        print "lectorrrrr"
        print lector
        ejemplar = Ejemplar.objects.get(codigo_barras=self.kwargs.get('codigo'))

        hoy = datetime.now()
        dia = hoy.isoweekday()

        if dia == 5:
            # si es viernes se suma 3 dias al la fecha de entrega
            fecha_entrega = hoy + timedelta(days=3)
        else:
            # si el dia es distinto de viernes sol ose suma 1 dia
            fecha_entrega = hoy + timedelta(days=1)

        # Guardamos el prestamo
        prestamo = Prestamo(
            bibliotecario=bibliotecario,
            lector=lector,
            ejemplar=ejemplar,
            fecha_entrega=fecha_entrega
        )
        print "vamo presmo"
        prestamo.save()

        # ponemos el libro como Prestado y guardamos
        ejemplar.prestado = True
        ejemplar.save()

        return redirect('circulacion_app:printVoucher', pk=prestamo.pk)

class VoucherView(SingleObjectMixin, View):
    model = Prestamo

    def get(self, request, *args, **kwargs):
        prestamo = self.get_object()
        return generar_pdf(
            'circulacion/prestamo/print_voucher.html',
            {'pagesize' : 'A4', 'prestamo' : prestamo}
        )

class DevolverView(FormView):
    form_class = DevolucionForm
    template_name = 'circulacion/devolucion/devolucion.html'
    success_url = reverse_lazy('circulacion_app:devolverDetalle')

    def form_valid(self, form):
        # recuperamos los datos del bibliotecario
        bibliotecario = self.request.user
        # recuperar codigo del libro
        codigo = form.cleaned_data["codigo"]
        # recuperamos la hora y fecha actual
        fecha_devolucion = date.today()
        # recuperamos el prestamo decuardo al codigo de barras
        prestamo = Prestamo.objects.get(ejemplar__codigo_barras=codigo, devuelto=False)
        # Cambiamos el estado del prestamo a falso y lo guardamos
        prestamo.ejemplar.prestado = False
        prestamo.ejemplar.save()
        prestamo.devuelto = True
        prestamo.save()
        devolucion = Devolucion(
            prestamo=prestamo,
            bibliotecario=bibliotecario,
            fecha_devolucion=fecha_devolucion,
        )
        devolucion.save()
        return redirect('circulacion_app:devolverDetalle', pk=prestamo.pk)


class DetalleDevolucionView(DetailView):
    model = Prestamo
    template_name = 'circulacion/devolucion/detalle_devolucion.html'

from django.shortcuts import render, render_to_response

class ReporteDeudoresView(SingleObjectMixin, FormMixin, TemplateView):

    form_class = DeudoresForm

    def get(self, request, *args, **kwargs):
        usuario = self.request.user
        if request.method == 'GET':
            form2 = DeudoresForm(request.GET)
            if form2.is_valid():
                #Recuperar valores
                hoy = datetime.now()
                categoria = request.GET.get('tipo_lector','')
                print categoria
                if categoria:
                    categoria =  TipoLector.objects.get(id=categoria)
                
                results = Prestamo.objects.filter(Q(fecha_entrega__lte=hoy), Q(devuelto=False), Q(lector__tipo=categoria))
                
                print results

                #datos para el pdf
                fecha = datetime.now() #fecha actual
                formatofecha = fecha.strftime("%d/%m/%Y") 
                return generar_pdf('reporte/reporte_deudores.html', {'pagesize':'A4', 'fecha': formatofecha, 'resultado': results, 'tipo': categoria})
            else: #formulario no valido
                form2 = DeudoresForm(request.GET)

        return render_to_response('reporte/form_deudores.html',{'form2': form2, 'user':usuario})