from django.contrib import admin
from .models import TipoAutor, Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ['apellidos_y_nombres']
    ordering = ['apellidos_y_nombres']
    search_fields = ('apellidos_y_nombres',)

admin.site.register(TipoAutor)
admin.site.register(Autor, AutorAdmin)
