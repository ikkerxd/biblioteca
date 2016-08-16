from django.contrib import admin
from .models import TipoMaterial, Material, Descriptor, Ejemplar


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['titulo','isbn','titulo_secundario', 'tipo_material','usuario']
    ordering = ['titulo']
    search_fields = ('titulo__unaccent','isbn__unaccent','titulo_secundario__unaccent', 'tipo_material__nombre__unaccent','usuario__username__unaccent')

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()


class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['nombre_Material','isbn_Material','numero_ingreso', 'signatura', 'codigo_barras', 'ubicacion','usuario',]
    ordering = ['material']
    search_fields = ('material__titulo__unaccent','material__isbn__unaccent','numero_ingreso__unaccent', 'signatura__unaccent', 'codigo_barras__unaccent','ubicacion__nombre__unaccent','usuario__username__unaccent')

    def nombre_Material(self, obj):
        return obj.material.titulo

    def isbn_Material(self, obj):
        return obj.material.isbn

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()


class DescriptorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    ordering = ['nombre']
    search_fields = ('nombre__unaccent',)

class TipoMaterialAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    ordering = ['nombre']
    search_fields = ('nombre__unaccent',)


admin.site.register(TipoMaterial,TipoMaterialAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Descriptor, DescriptorAdmin)

