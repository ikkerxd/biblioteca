# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0002_auto_20160605_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='devuelto',
            field=models.BooleanField(default=datetime.datetime(2016, 8, 3, 2, 57, 20, 591936, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
