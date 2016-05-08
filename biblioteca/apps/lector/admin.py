from django.contrib import admin
from .models import CarreraProfesional, TipoLector, Lector
from import_export.admin import ImportExportModelAdmin
from .resource import LectorResource
# Register your models here.
class LectorAdmin(ImportExportModelAdmin):
    resource_class = LectorResource
    list_display = ['codigo', 'carrera', 'dni', 'apellidos_y_nombres']
    ordering = ['codigo']
    search_fields = ('codigo', 'dni', 'apellidos_y_nombres')


admin.site.register(Lector, LectorAdmin)
admin.site.register(CarreraProfesional)
admin.site.register(TipoLector)
