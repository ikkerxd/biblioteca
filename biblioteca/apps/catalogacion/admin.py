from django.contrib import admin

from .models import TipoMaterial, Material, Descriptor, Ejemplar

admin.site.register(TipoMaterial)
admin.site.register(Material)
admin.site.register(Descriptor)
admin.site.register(Ejemplar)
