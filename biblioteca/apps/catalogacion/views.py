from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import Material, Ejemplar, TipoMaterial
from apps.autores.models import Autor
from django.db.models import Q
from .forms import BusquedaForm
from wkhtmltopdf.views import PDFTemplateView

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
    template_name = "catalogacion/busqueda.html"

    def get_context_data(self, **kwargs):
        context = super(BusquedaView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        ##Recuperar valores
        categoria = request.POST['categoria']
        if categoria:
            categoria =  TipoMaterial.objects.get(id=categoria)
        tipo = request.POST['tipo'] 
        buscar = request.POST['descripcion']
        palabras = buscar.split(" ")


        if tipo == 'titulo':
            for palabra in palabras:
                if categoria:
                    materiales = Material.objects.filter(titulo__icontains=palabra,tipo_material=categoria).distinct()
                else:
                    materiales = Material.objects.filter(titulo__icontains=palabra).distinct()
            return render(request,'catalogacion/busqueda.html',{'materiales':materiales, 'form':self.get_form})
        else:
            if tipo == 'autor':
                for palabra in palabras:
                    if categoria:
                        materiales = Material.objects.filter((Q(autor__nombres__icontains=palabra)|Q(autor__apellidos__icontains=palabra)),tipo_material=categoria).distinct()
                    else:
                        materiales = Material.objects.filter(Q(autor__nombres__icontains=palabra)|Q(autor__apellidos__icontains=palabra)).distinct()
                return render(request,'catalogacion/busqueda.html',{'materiales':materiales,'form':self.get_form})
            else:
                if tipo == 'signatura':
                    for palabra in palabras:
                        if categoria:
                            materiales = Material.objects.filter(signatura__icontains=palabra,tipo_material=categoria).distinct()
                        else:
                            materiales = Material.objects.filter(signatura__icontains=palabra).distinct()
                    return render(request,'catalogacion/busqueda.html',{'materiales':materiales, 'form':self.get_form})
                else:
                    if categoria:
                        for palabra in palabras:
                            materiales = Material.objects.filter(tipo_material=categoria).distinct()
                            print materiales
                        return render(request,'catalogacion/busqueda.html',{'materiales':materiales, 'form':self.get_form})
                    else:
                        for palabra in palabras:
                            materiales = Material.objects.filter(Q(autor__nombres__icontains=palabra)|Q(autor__apellidos__icontains=palabra)|Q(titulo__icontains=palabra)|Q(signatura__icontains=palabra)).distinct()
                            print materiales
                        return render(request,'catalogacion/busqueda.html',{'materiales':materiales, 'form':self.get_form})

class Materialdetail(SingleObjectMixin, View):

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

class VerReporteAutor(SingleObjectMixin, View):

    model = Autor

    def get(self, request, *args, **kwargs):
        fecha = datetime.now() #fecha actual
        formatofecha = fecha.strftime("%d/%m/%Y") 
        autor = self.get_object()
        materiales = Material.objects.filter(Q(autor__nombres__icontains=autor.nombres),Q(autor__apellidos__icontains=autor.apellidos)).distinct()
        html = render_to_string('reporte/reporte_autor.html', {'pagesize':'A4', 'materiales':materiales, 'fecha': formatofecha, 'autor':autor}, context_instance=RequestContext(request))
        return generar_pdf(html)

class MyPDF(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'reporte/reporte_auto.html'
    cmd_options = {
        'margin-top': 3,
    }