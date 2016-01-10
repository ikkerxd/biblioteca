# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=8, verbose_name=b'username')),
                ('email', models.EmailField(max_length=254, verbose_name=b'correo electronico')),
                ('first_name', models.CharField(max_length=50, verbose_name=b'nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'apellidos')),
                ('avatar', models.ImageField(upload_to=b'users')),
                ('address', models.CharField(max_length=50, verbose_name=b'direccion')),
                ('phone', models.CharField(max_length=50, verbose_name=b'telefono')),
                ('gender', models.CharField(max_length=1, verbose_name=b'sexo', choices=[(b'M', b'MASCULINO'), (b'F', b'FEMENINO')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
