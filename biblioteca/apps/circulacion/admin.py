from django.contrib import admin
from .models import Prestamo, Devolucion

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['bibliotecario', 'lector', 'ejemplar', 'fecha_entrega']
    ordering = ['fecha_entrega']
    search_fields = ('lector', 'bibliotecario',)

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ['prestamo', 'bibliotecario', 'fecha_devolucion']
    ordering = ['fecha_devolucion']
    search_fields = ('prestamo', 'bibliotecario',)

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Devolucion, DevolucionAdmin)
