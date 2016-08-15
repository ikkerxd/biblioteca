# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalogacion', '0006_ejemplar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
