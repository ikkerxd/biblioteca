from django.contrib import admin
from .models import Prestamo, Devolucion, Semestre

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['bibliotecario', 'lector', 'ejemplar', 'fecha_entrega']
    ordering = ['fecha_entrega']
    search_fields = ('lector', 'bibliotecario',)

    def save_model(self, request, obj, form, change):
        obj.bibliotecario = request.user
        obj.save()

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ['prestamo', 'bibliotecario', 'fecha_devolucion']
    ordering = ['fecha_devolucion']
    search_fields = ('prestamo', 'bibliotecario',)

    def save_model(self, request, obj, form, change):
        obj.bibliotecario = request.user
        obj.save()

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Devolucion, DevolucionAdmin)
admin.site.register(Semestre)
