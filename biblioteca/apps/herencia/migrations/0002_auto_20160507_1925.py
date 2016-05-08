# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'masculino'), (b'F', b'femenino')]),
        ),
    ]
