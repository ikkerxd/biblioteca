# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from apps.herencia.models import TimeStampModel
from apps.autores.models import Autor
from apps.lector.models import Biblioteca
from django_countries.fields import CountryField

class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo de Material'

    def __unicode__(self):
        return self.nombre


class Descriptor(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Descriptor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Material(TimeStampModel):
    portada = models.ImageField('Portada (Imagen)', upload_to='portada', blank=True, null=True)
    titulo = models.CharField('Titulo',max_length=200)
    titulo_secundario = models.CharField(
        'Título secundario',
        max_length=200,
        blank=True,
        null=True
    )
    tipo_material = models.ForeignKey(TipoMaterial)
    isbn = models.CharField('ISBN', max_length=50, blank=True, null=True,unique=True)
    autor = models.ManyToManyField(Autor, blank=True)
    archivo = models.FileField(upload_to='archivos', blank=True, null=True)
    pais = CountryField(blank_label='(Seleccione un Pais de Edicion)', blank=True, null=True)
    editorial = models.CharField(max_length=70, blank=True, null=True)
    anio = models.CharField('Año',max_length=20, blank=True, null=True)
    edicion = models.CharField(max_length=10,  blank=True, null=True)
    descriptores = models.ManyToManyField(Descriptor, blank=True) #palabras claves
    contenido = models.TextField(blank=True, null=True) #indice
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = 'Materiales'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Material, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s" % (self.titulo, self.isbn)

class ManagerEjemplar(models.Manager):

    def ejemplar_material(self, material):
        return self.filter(material=material).distinct()

ADQUISICION_CHOICES = (
    ('Compra', 'Compra'),
    ('Donacion', 'Donacion'),
    ('Otro', 'Otro'),
)

class Ejemplar(TimeStampModel):
    numero_ingreso = models.CharField('Número de ingreso', max_length=50,  blank=True, null=True)
    codigo_barras = models.CharField('Código de barras', max_length=50, blank=True, null=True,unique=True)
    material = models.ForeignKey(Material)
    #ubicacion = models.CharField('Ubicación', max_length=50, blank=True, null=True) #ejem: biblioteca central
    ubicacion = models.ForeignKey(Biblioteca,blank=True, null=True)
    signatura = models.CharField('Signatura topográfica', max_length=60, blank=True, null=True)
    precio = models.DecimalField('Precio normal en soles',max_digits=6, decimal_places=2, blank=True, null=True)
    numero_copia = models.CharField('Número de copia', max_length=20, blank=True, null=True)
    fuente_adquisicion = models.CharField('Fuente de adquisición',max_length=60, choices=ADQUISICION_CHOICES, null=True, blank=True) #compra, donacion
    observacion = models.CharField('Observación', max_length=400, blank=True, null=True)
    notas = models.CharField(max_length=50, blank=True, null=True) #Nota general: perdido, repuesto
    descripcion_fisica = models.TextField('Descripción Física', blank=True, null=True) #N° de pag, Dimensiones, Otros detalles
    prestado = models.BooleanField(default=False)
    objects = ManagerEjemplar()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    #user = models.ForeignKey(User,editable=False)

    class Meta:
        verbose_name_plural = 'Ejemplares'

    def __unicode__(self):
        return "%s %s" % (self.material.titulo, self.codigo_barras)
        #return self.material.titulo
