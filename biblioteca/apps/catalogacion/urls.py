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
    #url(r'^detalle/autor/(?P<pk>\d+)$', 
    #    AutorView.as_view(), 
    #    name='detalle_autor'
    #),
    #url(r'^reporte_autor/(?P<pk>\d+)/$', 
    #    VerReporteAutor.as_view(),
    #    name='verreporte'
    #),
    #url(r'^pdf/$',
    #    views.PDFTemplateView.as_view(template_name='reporte/reporte_auto.html', filename='my_pdf.pdf'), 
    #    name='pdf'),
    url(r'^pdf/$',
        views.MyPDF.as_view(), 
        name='pdf'),
]
