# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0005_auto_20160816_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(max_length=400, verbose_name=b'Titulo'),
        ),
    ]
