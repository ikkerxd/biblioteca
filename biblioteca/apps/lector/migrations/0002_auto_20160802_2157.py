# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='fecha_fin',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lector',
            name='fecha_inicio',
            field=models.DateField(null=True, blank=True),
        ),
    ]
