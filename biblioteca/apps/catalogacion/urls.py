from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.Index.as_view(),
        name="Index"
    ),
    url(
        r'^publicacion/(?P<pk>\d+)$',
        views.MaterialView.as_view(),
        name="material"
    ),
    
    # url(
    #     r'^busqueda/(?P<pk>\d+)$',
    #     views.BusquedaView.as_view(),
    #     name="busqueda"
    # ),
]
