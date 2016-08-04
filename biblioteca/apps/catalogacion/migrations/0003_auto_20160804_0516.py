# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0002_auto_20160605_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptor',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
