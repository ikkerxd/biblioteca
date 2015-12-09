from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.Index.as_view(),
        name="Index"
    ),
    url(
        r'^material/(?P<pk>\d+)$',
        views.MaterialView.as_view(),
        name="material"
    ),
    url(
        r'^busqueda/$',
        views.BusquedaView.as_view(),
        name="busqueda"
    ),
    url(
        r'^detalle/ver_pdf/(?P<pk>\d+)/$', 
        views.Materialdetail.as_view(), 
        name='ver_pdf'
    ),
]
