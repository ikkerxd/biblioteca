from django.contrib import admin
from .models import TipoAutor, Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ['apellidos_y_nombres','tipo_autor']
    ordering = ['apellidos_y_nombres']
    search_fields = ('apellidos_y_nombres__unaccent','tipo__nombre')

    def tipo_autor(self, obj):
        return ",\n".join([p.nombre for p in obj.tipo.all()])

admin.site.register(TipoAutor)
admin.site.register(Autor, AutorAdmin)
