# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0002_auto_20160108_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejemplar',
            old_name='Precio',
            new_name='precio',
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_ingreso',
            field=models.CharField(max_length=50, verbose_name=b'N\xc3\xbamero de ingreso'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='ubicacion',
            field=models.CharField(max_length=50, verbose_name=b'Ubicaci\xc3\xb3n'),
        ),
    ]
