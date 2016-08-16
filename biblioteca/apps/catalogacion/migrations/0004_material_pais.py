# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0003_auto_20160815_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='pais',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
