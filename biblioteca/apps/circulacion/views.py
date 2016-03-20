from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from django.core.urlresolvers import reverse_lazy

# local model import
from apps.lector.models import Lector

# Local Import
from .forms import LectorPrestamoForm


class LectorPrestamoView(FormView):
    template_name = 'circulacion/prestamo/prestamo.html'
    print 'Sali a prestamo'
    form_class = LectorPrestamoForm
    # success_url = reverse_lazy('users_app:login')
    def get_success_url(self):
        return reverse_lazy('users_app:login')

    # def get_success_url(self):
    #     return reverse_lazy('users_app:login')

    def form_valid(self, form):
        codigo = form.cleaned_data['lector']
        lector = Lector.objects.get(codigo=codigo)
        return redirect('circulacion_app:ejemplarPrestamo', pk=lector.pk)


class EjemplarPrestamoView(TemplateView):
    template_name = 'circulacion/prestamo/ejemplar.html'
