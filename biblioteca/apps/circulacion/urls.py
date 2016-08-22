from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/prestamo/$',
        views.LectorPrestamoView.as_view(),
        name="lectorPrestamo"
    ),
    url(
        r'^panel/prestamo/(?P<pk>\d+)/$',
        views.EjemplarPrestamoView.as_view(),
        name="ejemplarPrestamo"
    ),
    url(
        r'^panel/prestamo/confirmar/(?P<pk>\d+)/(?P<codigo>[\w-]+)/$',
        views.ConfirmarPrestamoView.as_view(),
        name="confirmarPrestamo"
    ),
    url(
        r'^panel/prestamo/registrar/(?P<pk>\d+)/(?P<codigo>[\w-]+)/$',
        views.RegistrarPrestamoView.as_view(),
        name="registarPrestamo"
    ),
    url(
        r'^panel/imprimir/voucher/prestamo/(?P<pk>\d+)/$',
        views.VoucherView.as_view(),
        name='printVoucher'
    ),
    url(
        r'^panel/devolucion/$',
        views.DevolverView.as_view(),
        name="devolver"
    ),
    url(
        r'^panel/devolucion/detalle/(?P<pk>\d+)/$',
        views.DetalleDevolucionView.as_view(),
        name="devolverDetalle"
    ),
    url(
        r'^deudores/$',
        views.ReporteDeudoresView.as_view(),
        name="reporteDeudores"
    ),
]
