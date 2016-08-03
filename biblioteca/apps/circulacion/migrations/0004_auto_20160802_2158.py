# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0003_prestamo_devuelto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='devuelto',
            field=models.BooleanField(default=False),
        ),
    ]
