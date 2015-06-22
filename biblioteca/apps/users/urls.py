from django.conf.urls import url
from .views import LogIn

urlpatterns = [
    url(r'^login/$', LogIn.as_view(), name="login"),
]
