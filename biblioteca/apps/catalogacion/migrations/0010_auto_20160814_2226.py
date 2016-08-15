# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0009_auto_20160814_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='usuario',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
