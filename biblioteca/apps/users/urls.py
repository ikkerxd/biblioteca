from django.conf.urls import url
from .views import LogIn, Index

urlpatterns = [
    url(r'^$', Index.as_view(), name="Index"),
    url(r'^login/$', LogIn.as_view(), name="login"),
    url(r'^salir/$', 'apps.users.views.LogOut', name="logout"),    
]
