# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0002_auto_20160815_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='pais',
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='codigo_barras',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name=b'C\xc3\xb3digo de barras', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='isbn',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name=b'ISBN', blank=True),
        ),
    ]
