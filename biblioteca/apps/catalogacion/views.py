# -*- coding: utf-8 -*- 
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, View, FormView
from .models import Material, Ejemplar, TipoMaterial
from apps.autores.models import Autor
from apps.circulacion.models import Prestamo

from django.db.models import Q
#from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


#pure-pagination
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
#from pure_pagination.mixins import PaginationMixin

from .forms import BusquedaForm, RevisarRegistroForm

from django.template.loader import render_to_string

from django.template import RequestContext
import cStringIO as StringIO
import ho.pisa as pisa
from datetime import datetime, date, time

class Index(FormMixin, TemplateView):
    form_class = BusquedaForm
    model = Material
    template_name = "catalogacion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['materiales'] = Material.objects.all()[:4]
        context['form'] = self.get_form()
        return context

class NosotrosView(FormMixin, TemplateView):
    form_class = BusquedaForm
    template_name = "catalogacion/nosotros.html"

    def get_context_data(self, **kwargs):
        context = super(NosotrosView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

class DirectorioView(FormMixin, TemplateView):
    form_class = BusquedaForm
    template_name = "catalogacion/directorio.html"

    def get_context_data(self, **kwargs):
        context = super(DirectorioView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

class ContactenosView(FormMixin, TemplateView):
    form_class = BusquedaForm
    template_name = "catalogacion/contactenos.html"

    def get_context_data(self, **kwargs):
        context = super(ContactenosView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

class MaterialView(FormMixin, DetailView):
    form_class = BusquedaForm
    model = Material
    template_name = "catalogacion/material.html"

    def get(self, request, *args, **kwargs):
    	self.object = self.get_object()
    	return super(MaterialView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MaterialView, self).get_context_data(**kwargs)
        material = self.object
        context['ejemplares'] = Ejemplar.objects.ejemplar_material(material)
        context['existencia'] = context['ejemplares'].count
        context['prestamos'] = Prestamo.objects.all().order_by('-created')
        context['form'] = self.get_form()
        return context

class BusquedaView(FormMixin, ListView):
    form_class = BusquedaForm
    model = Material
    model = TipoMaterial
    model = Ejemplar

    def get_context_data(self, **kwargs):
        context = super(BusquedaView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get(self, request, *args, **kwargs):
        #Recuperar valores
        if request.method=='GET':
            categoria = request.GET.get('categoria')
            if (categoria != ""):
                categoria =  TipoMaterial.objects.get(id=categoria)
            tipo = request.GET.get('tipo','')
            print "TIPO"
            print tipo
            query = request.GET.get('descripcion', '')

            if((categoria == "") and (tipo == "") and (query == "")):
                results = Material.objects.all()
            else:
                if((categoria != "") and (tipo == "") and (query == "")):
                    results = Material.objects.filter(Q(tipo_material = categoria)).distinct()
                else:
                    if((categoria != "") and (tipo == "") and (query != "")):
                        results = Material.objects.filter(Q(tipo_material = categoria) & (Q(titulo__unaccent__icontains = query)|Q(autor__slug__unaccent__icontains = query))).distinct()
                    else:
                        if ((categoria == "") and (tipo != "") and (query != "")):
                            if tipo == 'titulo':
                                results = Material.objects.filter(Q(titulo__unaccent__icontains = query)).distinct()
                            else:
                                if tipo == 'autor':
                                    results = Material.objects.filter(Q(autor__slug__unaccent__icontains = query)).distinct()
                                else:
                                    if tipo == 'signatura':
                                        print "ENTRO 1"
                                        tempresult = Ejemplar.objects.filter(Q(signatura__icontains= query)).values_list('material', flat=True).distinct()
                                        print "results temp"
                                        print tempresult                                        
                                        results = Material.objects.filter(id__in=tempresult)
                                        print "results"
                                        print results
                        else:
                            if ((categoria != "") and (tipo != "") and (query != "")):
                                if tipo == 'titulo':
                                    results = Material.objects.filter(Q(titulo__unaccent__icontains = query) &
                                                                            Q(tipo_material = categoria)
                                                                          ).distinct()
                                else:
                                    if tipo == 'autor':
                                        results = Material.objects.filter(Q(tipo_material = categoria ) & 
                                                              Q(autor__slug__unaccent__icontains = query) 
                                                             ).distinct()
                                    else:
                                        if tipo == 'signatura':
                                            tempresult = Ejemplar.objects.filter(Q(signatura__icontains= query)).values_list('material', flat=True).distinct()
                                            results = Material.objects.filter(id__in=tempresult)
                            else:
                                if ((categoria == "") and (tipo == "") and (query != "")) or ((categoria == "") and (tipo != "") and (query == "")):
                                    tempresult = Ejemplar.objects.filter(Q(signatura__icontains= query)).values_list('material', flat=True).distinct()
                                    results = Material.objects.filter(Q(titulo__unaccent__icontains = query)|Q(autor__slug__unaccent__icontains = query)|Q(id__in=tempresult)).distinct()
        total = results.count() #numero total de materiales encontrados
        parametros = request.GET.copy() 
        if parametros.has_key('page'):
            del parametros['page']
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(results, 10) #numero de items por pagina

        queryset = p.page(page)

        context = {
                'materiales':queryset,
                'parametros':parametros,
                'form':self.get_form,
                'total':total
        }
        return render(request, 'catalogacion/busqueda.html', context)

#Materialdetail
class LeerPDFDoc(SingleObjectMixin, View):

    model = Material

    def get(self, request, *args, **kwargs):
        nombre = self.get_object().archivo
        archivo = 'media/'+ str(nombre)
        with open(archivo, 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
        pdf.closed


class AutorView(SingleObjectMixin, TemplateView):
    template_name = 'catalogacion/detalle_autor.html.html'
    model = Autor

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AutorView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AutorView, self).get_context_data(**kwargs)
        context['materiales'] = self.object.material_set.all().order_by('-created')[:3]
        return context

def generar_pdf(html):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf') #mimetype
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

class TiposDeMaterialView(TemplateView):
    model = TipoMaterial
    template_name = "catalogacion/include/header.html"

    def get_context_data(self, **kwargs):
        context = super(TiposDeMaterialView, self).get_context_data(**kwargs)
        context['tiposmat'] = TipoMaterial.objects.all()
        return context


class VerReporteAutor(SingleObjectMixin, View):

    model = Autor

    def get(self, request, *args, **kwargs):
        fecha = datetime.now() #fecha actual
        formatofecha = fecha.strftime("%d/%m/%Y")
        autor = self.get_object()
        materiales = Material.objects.filter(Q(autor__apellidos_y_nombres__icontains=autor)).distinct()
        html = render_to_string('reporte/reporte_autor.html', {'pagesize':'A4', 'materiales':materiales, 'fecha': formatofecha, 'autor':autor}, context_instance=RequestContext(request))
        return generar_pdf(html)

class RevisarRegistroView(SingleObjectMixin, FormMixin, TemplateView):

    form_class = BusquedaForm

    def get(self, request, *args, **kwargs):
        usuario = self.request.user
        if request.method == 'GET':
            form2 = RevisarRegistroForm(request.GET)
            if form2.is_valid():
                qset = Q()
                qset2 = Q()
                #Recuperar valores
                categoria = request.GET.get('categoria','')

                query =  request.GET.get('descripcion', '')

                fecha_inicio_aux = request.GET.get('Mostrar_desde', '')
                fecha_inicio = datetime.strptime(fecha_inicio_aux +" 00:00:00", "%d/%m/%Y %H:%M:%S")

                fecha_fin_aux = request.GET.get('Mostrar_hasta', '')
                fecha_fin = datetime.strptime(fecha_fin_aux +" 23:59:59", "%d/%m/%Y %H:%M:%S")
                
                opcion = request.GET.get('opcion')

                #Realizamos la consulta
                if opcion == 'prestados':
                    #qset.add(Q(prestado=True), qset.AND)
                    if categoria:
                        categoria =  TipoMaterial.objects.get(id=categoria)
                        qset2.add(Q(ejemplar__material__tipo_material=categoria), qset2.AND)
                    if query:
                        qset2.add(Q(ejemplar__material__titulo__unaccent__icontains=query) | Q(ejemplar__material__autor__slug__unaccent__icontains = query) , qset2.AND)

                    if (fecha_inicio and fecha_fin):
                        qset2.add(Q(created__range=[fecha_inicio, fecha_fin]), qset2.AND)
                    
                    consulta = Prestamo.objects.filter(qset2).distinct().order_by('ejemplar__ubicacion')
                else:
                    if categoria:
                        categoria =  TipoMaterial.objects.get(id=categoria)
                        qset.add(Q(material__tipo_material=categoria), qset.AND)
                    if query:
                        qset.add(Q(material__titulo__unaccent__icontains=query) | Q(material__autor__slug__unaccent__icontains = query) , qset.AND)

                    if (fecha_inicio and fecha_fin):
                        qset.add(Q(created__range=[fecha_inicio, fecha_fin]), qset.AND)

                    consulta = Ejemplar.objects.filter(qset).distinct().order_by('ubicacion')

                results = consulta
                print results

                #datos para el pdf
                fecha = datetime.now() #fecha actual
                formatofecha = fecha.strftime("%d/%m/%Y") 
                html = render_to_string('reporte/reporte_revisar_registros.html', {'pagesize':'A4', 'fecha': formatofecha, 'resultado': results,'opcion':opcion}, context_instance=RequestContext(request))
                return generar_pdf(html)
        else: #formulario no valido
            form2 = RevisarRegistroForm(request.GET)
        return render_to_response('reporte/revisar_registros.html',{'form2': form2,'user':usuario})


