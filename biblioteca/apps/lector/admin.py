from django.contrib import admin
from .models import CarreraProfesional, TipoLector, Lector, Biblioteca
from import_export.admin import ImportExportModelAdmin
from .resource import LectorResource
# Register your models here.
class LectorAdmin(ImportExportModelAdmin):
    resource_class = LectorResource
    list_display = ['codigo', 'dni', 'carrera','apellidos_y_nombres']
    ordering = ['codigo']
    search_fields = ('codigo__unaccent', 'dni__unaccent', 'apellidos_y_nombres__unaccent')


class CarreraProfesionalAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']
    ordering = ['codigo']
    search_fields = ('codigo__unaccent','nombre__unaccent')

class TipoLectorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    ordering = ['nombre']
    search_fields = ('nombre__unaccent',)


admin.site.register(Lector, LectorAdmin)
admin.site.register(CarreraProfesional,CarreraProfesionalAdmin)
admin.site.register(TipoLector,TipoLectorAdmin)
