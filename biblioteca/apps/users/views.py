from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from django.core.urlresolvers import reverse_lazy

from .forms import LoginForm


class LogIn(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        print 'hola'
        return super(LogIn, self).form_valid(form)
