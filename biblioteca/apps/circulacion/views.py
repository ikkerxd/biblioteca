from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from django.core.urlresolvers import reverse_lazy

# Local Import
from .forms import LectorPrestamoForm


class LectorPrestamoView(TemplateView):
    print 'entre a prestamo'
    template_name = 'circulacion/prestamo/prestamo.html'
    print 'Sali a prestamo'
    form_class = LectorPrestamoForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        print 'entre a prestamso'
        return super(LectorPrestamoView, self).form_valid(form)


class EjemplarPrestamoView(TemplateView):
    template_name = 'circulacion/prestamo/ejemplar.html'
