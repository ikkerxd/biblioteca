# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.TimeStampModel')),
                ('apellidos_y_nombres', models.CharField(max_length=160)),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'masculino'), (b'F', b'femenino')])),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
            ],
            bases=('herencia.timestampmodel',),
        ),
    ]
