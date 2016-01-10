from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import Material, Ejemplar, TipoMaterial
from apps.autores.models import Autor

from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from .forms import BusquedaForm
from wkhtmltopdf.views import PDFTemplateView
from django.template.loader import render_to_string

from django.template import RequestContext
import cStringIO as StringIO
import ho.pisa as pisa
from datetime import datetime

class Index(FormMixin, TemplateView):
    form_class = BusquedaForm
    model = Material
    template_name = "catalogacion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['materiales'] = Material.objects.all()[:4]
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
        context['form'] = self.get_form()
        return context

class BusquedaView(FormMixin, ListView):
    form_class = BusquedaForm
    model = Material
    model = TipoMaterial

    def get_context_data(self, **kwargs):
        context = super(BusquedaView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get(self, request, *args, **kwargs):
        #Recuperar valores
        categoria = request.GET.get('categoria','')
        if categoria:
            categoria =  TipoMaterial.objects.get(id=categoria)
        tipo = request.GET.get('tipo','')
        query = request.GET.get('descripcion', '')

        if tipo == 'titulo':
            if categoria:
                qset = (
                    Q(titulo__icontains = query) & Q(tipo_material = categoria) 
                )
            else:
                 qset = ( Q(titulo__icontains = query) )
        else:
            if tipo == 'autor':
                if categoria:  
                    qset = (
                        Q(tipo_material = categoria ) & 
                       ( Q(autor__nombres__icontains = query) | 
                        Q(autor__apellidos__icontains = query))
                    )
                else:
                    qset = (
                        Q(autor__nombres__icontains = query) | 
                        Q(autor__apellidos__icontains = query)
                    )
            else:
                if tipo == 'signatura':
                    qset = ()
                else:
                    if categoria:
                        qset = (
                            Q(tipo_material=categoria) 
                        )
                    else:
                        qset = (
                            Q(titulo__icontains=query) |
                            Q(autor__nombres__icontains=query) | 
                            Q(autor__apellidos__icontains=query)
                        )

        results = Material.objects.filter(qset).distinct()

        paginator = Paginator(results,1) # se indica items por pagina
        page = request.GET.get('page')

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        # If page request (9999) is out of range, deliver last page of results.
        try:
            materialespag = paginator.page(page)
        except (EmptyPage, InvalidPage):
            materialespag = paginator.page(paginator.num_pages)

        return render_to_response('catalogacion/busqueda.html', {'filter': results,
                                                'materiales': materialespag,
                                                'form':self.get_form
                                                }, context_instance=RequestContext(request))
#Materialdetail
class LeerPDFDoc(SingleObjectMixin, View):

    model = Ejemplar

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

class VerReporteAutor(SingleObjectMixin, View):

    model = Autor

    def get(self, request, *args, **kwargs):
        fecha = datetime.now() #fecha actual
        formatofecha = fecha.strftime("%d/%m/%Y") 
        autor = self.get_object()
        materiales = Material.objects.filter(Q(autor__nombres__icontains=autor.nombres),Q(autor__apellidos__icontains=autor.apellidos)).distinct()
        html = render_to_string('reporte/reporte_autor.html', {'pagesize':'A4', 'materiales':materiales, 'fecha': formatofecha, 'autor':autor}, context_instance=RequestContext(request))
        return generar_pdf(html)
