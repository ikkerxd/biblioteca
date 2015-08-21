from django.contrib import admin
from .models import TipoAutor, Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos']
    ordering = ['apellidos']
    search_fields = ('nombres', 'apellidos',)

admin.site.register(TipoAutor)
admin.site.register(Autor, AutorAdmin)
