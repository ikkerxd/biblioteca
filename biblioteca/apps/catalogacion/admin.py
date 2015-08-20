from django.contrib import admin
from .models import TipoMaterial, Material, Descriptor, Ejemplar


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'sigantura', 'titulo', 'tipo_material']
    ordering = ['titulo']
    search_fields = ('isbn', 'sigantura', 'titulo', 'tipo_material',)

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['numero_ingreso', 'material']
    ordering = ['material']
    search_fields = ('numero_ingreso', 'material',)
    
admin.site.register(TipoMaterial)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Descriptor)
admin.site.register(Ejemplar)
