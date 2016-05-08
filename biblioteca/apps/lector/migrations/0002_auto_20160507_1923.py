# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='direccion',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lector',
            name='dni',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
