from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, FormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin

from django.core.urlresolvers import reverse_lazy

# local model import
from apps.lector.models import Lector
from apps.circulacion.models import Ejemplar
from .models import Prestamo

# Local Import
from .functions import generar_pdf
from .forms import LectorPrestamoForm, LibroPrestamoForm
from datetime import datetime, timedelta


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
    Relizacino del prestamos si el dia es viernes
    el mismo se devolvera el viernes
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
            ejemplar__prestado=True
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
        # recuperar codigo del libro
        codigo = form.cleaned_data["codigo"]
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


class VoucherView(SingleObjectMixin, View):
    model = Prestamo

    def get(self, request, *args, **kwargs):
        prestamo = self.get_object()
        return generar_pdf(
            'circulacion/prestamo/print_voucher.html',
            {'pagesize' : 'A4', 'minombre' : 'hennry joel'}
        )
