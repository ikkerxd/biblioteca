from django.contrib import admin
from .models import CarreraProfesional, TipoLector, Lector
# Register your models here.
class LectorAdmin(admin.ModelAdmin):
    list_display = ['Codigo', 'carrera', 'dni', 'nombres', 'apellidos']
    ordering = ['Codigo']
    search_fields = ('Codigo', 'dni', 'nombres', 'apellidos',)

admin.site.register(Lector, LectorAdmin)
admin.site.register(CarreraProfesional)
admin.site.register(TipoLector)
