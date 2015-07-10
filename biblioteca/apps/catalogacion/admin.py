from django.contrib import admin

from .models import TipoMaterial, Material, KeyWord, Ejemplar

admin.site.register(TipoMaterial)
admin.site.register(Material)
admin.site.register(KeyWord)
admin.site.register(Ejemplar)
