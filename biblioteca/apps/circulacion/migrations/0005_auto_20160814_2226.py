# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0004_auto_20160802_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='bibliotecario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='bibliotecario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
