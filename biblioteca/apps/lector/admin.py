from django.contrib import admin
from .models import CarreraProfesional, TipoLector, Lector
# Register your models here.

admin.site.register(Lector)
admin.site.register(CarreraProfesional)
admin.site.register(TipoLector)
