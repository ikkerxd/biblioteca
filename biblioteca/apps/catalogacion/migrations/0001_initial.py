# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('herencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.TimeStampModel')),
                ('portada', models.ImageField(null=True, upload_to=b'portada', blank=True)),
                ('numero_ingreso', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=400)),
                ('prestado', models.BooleanField(default=False)),
                ('pais', models.CharField(max_length=50, verbose_name=b'lugar de edicion')),
                ('editorial', models.CharField(max_length=70)),
                ('descripcion_fisica', models.TextField()),
                ('dimensiones', models.TextField()),
                ('notas', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('archivo', models.FileField(upload_to=b'archivos')),
            ],
            options={
                'verbose_name_plural': 'Ejemplares',
            },
            bases=('herencia.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.TimeStampModel')),
                ('titulo', models.CharField(max_length=50)),
                ('titulo_secundario', models.CharField(max_length=70, null=True, blank=True)),
                ('isbn', models.CharField(max_length=50, null=True, verbose_name=b'ISBN', blank=True)),
                ('sigantura', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('autor', models.ManyToManyField(to='autores.Autor')),
            ],
            options={
                'verbose_name_plural': 'Materiales',
            },
            bases=('herencia.timestampmodel',),
        ),
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Material',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='tipo_material',
            field=models.ForeignKey(blank=True, to='catalogacion.TipoMaterial', null=True),
        ),
    ]
