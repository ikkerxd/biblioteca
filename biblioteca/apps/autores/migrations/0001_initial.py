# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
        ('herencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='herencia.Persona')),
                ('Codigo', models.CharField(max_length=30, null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'imagen_autor', blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('carrera', models.ForeignKey(blank=True, to='lector.CarreraProfesional', null=True)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
            bases=('herencia.persona',),
        ),
        migrations.CreateModel(
            name='TipoAutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipo Autor',
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='tipo',
            field=models.ManyToManyField(to='autores.TipoAutor'),
        ),
    ]
