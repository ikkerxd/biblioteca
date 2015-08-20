from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
    ordering = ['username']
    search_fields = ('username',)
# Register your models here.
admin.site.register(User, UserAdmin)