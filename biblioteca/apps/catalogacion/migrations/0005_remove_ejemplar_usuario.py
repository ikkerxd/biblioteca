# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0004_ejemplar_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='usuario',
        ),
    ]
