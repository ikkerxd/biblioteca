from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):
	fieldsets = (
		('Usuario', {'fields' : ('username', 'password')}),
		('Informacion del usuario' , {'fields' : ('first_name',
										'last_name',
										'email',
										'avatar')}),
		('Permisos' , {'fields' : ('is_active',
										'is_staff',
										'is_superuser',
										'groups',
										'user_permissions')}),

		)
admin.site.register(User, UserAdmin)

