# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Bibliotecas',
            },
        ),
        migrations.CreateModel(
            name='CarreraProfesional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=2)),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Carreras Profesionales',
            },
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.Persona')),
                ('codigo', models.CharField(unique=True, max_length=30)),
                ('dni', models.CharField(max_length=8, null=True, blank=True)),
                ('direccion', models.CharField(max_length=80, null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'imagen_lector', blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('slug', models.SlugField(editable=False)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_fin', models.DateField(null=True, blank=True)),
                ('carrera', models.ForeignKey(blank=True, to='lector.CarreraProfesional', null=True)),
            ],
            options={
                'verbose_name_plural': 'Lectores',
            },
            bases=('herencia.persona',),
        ),
        migrations.CreateModel(
            name='TipoLector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipo Lector',
            },
        ),
        migrations.AddField(
            model_name='lector',
            name='tipo',
            field=models.ForeignKey(blank=True, to='lector.TipoLector', null=True),
        ),
    ]
