# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0004_auto_20160108_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='archivo',
            field=models.FileField(null=True, upload_to=b'archivos', blank=True),
        ),
    ]
