from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/prestamo/$',
        views.LectorPrestamoView.as_view(),
        name="lectorPrestamo"
    ),
    url(
        r'^panel/prestamo/(?P<pk>\d+)$',
        views.EjemplarPrestamoView.as_view(),
        name="ejemplarPrestamo"
    ),

]
