# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0003_auto_20160108_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='material',
            name='titulo_secundario',
            field=models.CharField(max_length=200, null=True, verbose_name=b'T\xc3\xadtulo secundario', blank=True),
        ),
    ]
