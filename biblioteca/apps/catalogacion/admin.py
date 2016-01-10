from django.contrib import admin
from .models import TipoMaterial, Material, Descriptor, Ejemplar


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['isbn','titulo','titulo_secundario', 'tipo_material']
    ordering = ['titulo']
    search_fields = ('isbn','titulo','titulo_secundario', 'tipo_material',)


class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['numero_ingreso', 'signatura', 'codigo_barras', 'material']
    ordering = ['material']
    search_fields = ('numero_ingreso', 'signatura', 'codigo_barras','material',)

admin.site.register(TipoMaterial)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Descriptor)
