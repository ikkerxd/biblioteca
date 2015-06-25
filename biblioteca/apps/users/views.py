from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse_lazy

from .forms import LoginForm


class LogIn(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(LogIn, self).form_valid(form)


def LogOut(request):
    logout(request)
    return redirect('/')


class Index(TemplateView):
    template_name = 'users/index.html'
