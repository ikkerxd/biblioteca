# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0006_auto_20160817_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.SlugField(max_length=400, editable=False),
        ),
    ]
