from django.contrib import admin
from .models import Prestamo, Devolucion, Semestre, Biblioteca

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['bibliotecario', 'lector', 'codigo_lector','titulo_del_item_prestado','codigo_de_barras_del_item_prestado', 'created']
    ordering = ['created']
    search_fields = ('bibliotecario__username__unaccent','lector__apellidos_y_nombres__unaccent', 'lector__codigo__unaccent','ejemplar__material__titulo__unaccent','ejemplar__codigo_barras__unaccent','created')

    def codigo_lector(self, obj):
        return obj.lector.codigo

    def titulo_del_item_prestado(self, obj):
        return obj.ejemplar.material.titulo

    def codigo_de_barras_del_item_prestado(self, obj):
        return obj.ejemplar.codigo_barras

    def fecha_del_prestamo(self, obj):
        return obj.created

    def save_model(self, request, obj, form, change):
        obj.bibliotecario = request.user
        obj.save()

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ['nombre_lector', 'codigo_lector','codigo_de_barras_item_prestado','bibliotecario', 'fecha_devolucion']
    ordering = ['fecha_devolucion']
    search_fields = ('prestamo__lector__apellidos_y_nombres__unaccent', 'prestamo__lector__codigo__unaccent','prestamo__ejemplar__codigo_barras__unaccent','bibliotecario__username__unaccent','fecha_devolucion')

    def nombre_lector(self, obj):
        return obj.prestamo.lector

    def codigo_lector(self, obj):
        return obj.prestamo.lector.codigo

    def codigo_de_barras_item_prestado(self, obj):
        return obj.prestamo.ejemplar.codigo_barras

    def save_model(self, request, obj, form, change):
        obj.bibliotecario = request.user
        obj.save()

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Devolucion, DevolucionAdmin)
#admin.site.register(Semestre)
admin.site.register(Biblioteca)
