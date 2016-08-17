# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0002_auto_20160815_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='biblioteca',
        ),
    ]
