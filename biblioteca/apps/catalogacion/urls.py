from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.Index.as_view(),
        name="Index"
    ),
    url(
        r'^conozcanos/$',
        views.NosotrosView.as_view(),
        name="nosotros"
    ),
    url(
        r'^directorio/$',
        views.DirectorioView.as_view(),
        name="directorio"
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
        views.LeerPDFDoc.as_view(), 
        name='ver_pdf'
    ),
    url(r'^reporte_autor/(?P<pk>\d+)/$', 
        views.VerReporteAutor.as_view(),
        name='verreporte'
    ),
    url(r'^revisar_registros_del_sistema/$', 
        views.RevisarRegistroView.as_view(),
        name='RevisarRegistro'
    ),
    url(
        r'^$',
        views.TiposDeMaterialView.as_view(),
        name="tipos"
    )
]
