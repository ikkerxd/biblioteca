# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
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
            name='usuario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
