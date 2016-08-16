from django.contrib import admin

from .models import Bibliotecario
# Register your models here.
class BibliotecarioAdmin(admin.ModelAdmin):
    list_display = ['user','apellido_del_usuario','nombre_del_usuario','biblioteca']
    ordering = ['user']
    search_fields = ('user__username__unaccent','biblioteca__nombre__unaccent','user__last_name__unaccent','user__first_name__unaccent')

    def nombre_del_usuario(self, obj):
        return obj.user.first_name

    def apellido_del_usuario(self, obj):
        return obj.user.last_name

admin.site.register(Bibliotecario,BibliotecarioAdmin)
