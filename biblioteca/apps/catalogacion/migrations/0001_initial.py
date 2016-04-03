# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


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
                ('numero_ingreso', models.CharField(max_length=50, null=True, verbose_name=b'N\xc3\xbamero de ingreso', blank=True)),
                ('codigo_barras', models.CharField(max_length=50, null=True, verbose_name=b'C\xc3\xb3digo de barras', blank=True)),
                ('ubicacion', models.CharField(max_length=50, null=True, verbose_name=b'Ubicaci\xc3\xb3n', blank=True)),
                ('signatura', models.CharField(max_length=60, null=True, verbose_name=b'Signatura topogr\xc3\xa1fica', blank=True)),
                ('precio', models.DecimalField(null=True, verbose_name=b'Precio normal en soles', max_digits=6, decimal_places=2, blank=True)),
                ('numero_copia', models.CharField(max_length=20, null=True, verbose_name=b'N\xc3\xbamero de copia', blank=True)),
                ('fuente_adquisicion', models.CharField(max_length=60, verbose_name=b'Fuente de adquisici\xc3\xb3n')),
                ('observacion', models.CharField(max_length=400, null=True, verbose_name=b'Observaci\xc3\xb3n', blank=True)),
                ('notas', models.CharField(max_length=50, null=True, blank=True)),
                ('descripcion_fisica', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n F\xc3\xadsica', blank=True)),
                ('prestado', models.BooleanField(default=False)),
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
                ('portada', models.ImageField(null=True, upload_to=b'portada', blank=True)),
                ('titulo', models.CharField(max_length=200, verbose_name=b'Titulo')),
                ('titulo_secundario', models.CharField(max_length=200, null=True, verbose_name=b'T\xc3\xadtulo secundario', blank=True)),
                ('isbn', models.CharField(max_length=50, null=True, verbose_name=b'ISBN', blank=True)),
                ('archivo', models.FileField(null=True, upload_to=b'archivos', blank=True)),
                ('pais', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('editorial', models.CharField(max_length=70, null=True, blank=True)),
                ('anio', models.CharField(max_length=20, null=True, verbose_name=b'A\xc3\xb1o', blank=True)),
                ('edicion', models.CharField(max_length=10, null=True, blank=True)),
                ('contenido', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField()),
                ('autor', models.ManyToManyField(to='autores.Autor')),
                ('descriptores', models.ManyToManyField(to='catalogacion.Descriptor')),
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
            field=models.ForeignKey(to='catalogacion.TipoMaterial'),
        ),
    ]
