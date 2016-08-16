# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0004_material_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='portada',
            field=models.ImageField(upload_to=b'portada', null=True, verbose_name=b'Portada (Imagen)', blank=True),
        ),
    ]
