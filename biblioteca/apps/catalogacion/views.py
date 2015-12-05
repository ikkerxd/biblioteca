from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Material, Ejemplar
from django.db.models import Q

class Index(TemplateView):
    template_name = "catalogacion/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['materiales'] = Material.objects.all()[:4]
        print context['materiales'][0].signatura
        return context

class MaterialView(DetailView):
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
        return context

