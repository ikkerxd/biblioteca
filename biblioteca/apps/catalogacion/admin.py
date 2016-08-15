from django.contrib import admin
from .models import TipoMaterial, Material, Descriptor, Ejemplar


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['titulo','isbn','titulo_secundario', 'tipo_material']
    ordering = ['titulo']
    search_fields = ('titulo','isbn','titulo_secundario', 'tipo_material',)
    exclude = (' usuario',)

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()


class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['numero_ingreso', 'signatura', 'codigo_barras', 'material']
    ordering = ['material']
    search_fields = ('numero_ingreso', 'signatura', 'codigo_barras','material',)
    exclude = (' usuario',)

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()


admin.site.register(TipoMaterial)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Descriptor)

