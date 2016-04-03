# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_devolucion', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Devoluciones',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.TimeStampModel')),
                ('fecha_entrega', models.DateField()),
            ],
            bases=('herencia.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('inicio_semestre', models.DateField()),
                ('fin_semestre', models.DateField()),
            ],
        ),
    ]
