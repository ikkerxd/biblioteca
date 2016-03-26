# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('circulacion', '0001_initial'),
        ('catalogacion', '0002_auto_20160326_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='bibliotecario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='ejemplar',
            field=models.ForeignKey(to='catalogacion.Ejemplar'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='lector',
            field=models.ForeignKey(to='lector.Lector'),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='bibliotecario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='prestamo',
            field=models.ForeignKey(to='circulacion.Prestamo'),
        ),
    ]
