# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0010_auto_20160814_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='fuente_adquisicion',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Fuente de adquisici\xc3\xb3n', choices=[(b'Compra', b'Compra'), (b'Donacion', b'Donacion'), (b'Otro', b'Otro')]),
        ),
    ]
