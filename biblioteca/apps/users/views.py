from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse_lazy

from .forms import LoginForm
from django.db.models import Q
from apps.users.models import User
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import Group


class LogIn(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users_app:Panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
                #recuperamos el nombre del usuario
                nombreuser = user.username
                print "username"
                print nombreuser
                consulta = User.objects.filter(Q(username=nombreuser)&Q(groups__name='catalogador'))
                if consulta:
                    #si el usuario pertence al grupo catalogador
                    return redirect('/admin')
                consulta = User.objects.filter(Q(username=nombreuser)&Q(groups__name='bibliotecario'))
                if consulta:
                    #si el usuario pertence al grupo bibliotecario
                    return super(LogIn, self).form_valid(form)     

        return super(LogIn, self).form_valid(form)
        
    
def LogOut(request):
    logout(request)
    return redirect('/')


class Index(TemplateView):
    template_name = 'users/index.html'


class PanelView(TemplateView):
    template_name = 'users/panel/panel.html'
