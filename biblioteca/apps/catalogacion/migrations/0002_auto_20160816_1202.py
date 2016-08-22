# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='usuario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='material',
            field=models.ForeignKey(to='catalogacion.Material'),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='ubicacion',
            field=models.ForeignKey(blank=True, to='lector.Biblioteca', null=True),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='usuario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
