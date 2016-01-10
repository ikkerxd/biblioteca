# -*- coding: utf-8 -*- 
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from apps.herencia.models import TimeStampModel
from apps.autores.models import Autor
from django_countries.fields import CountryField

class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Tipo de Material'

    def __unicode__(self):
        return self.nombre


class Material(TimeStampModel):
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    titulo = models.CharField('Titulo',max_length=200)
    titulo_secundario = models.CharField('Título secundario',max_length=200, blank=True, null=True)
    tipo_material = models.ForeignKey(TipoMaterial, blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=50, blank=True, null=True)
    autor = models.ManyToManyField(Autor)
    pais = CountryField(blank_label='(Seleccione un pais)')
    editorial = models.CharField(max_length=70)
    anio = models.CharField('Año',max_length=20)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Materiales'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Material, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo


class Descriptor(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Descriptor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class ManagerEjemplar(models.Manager):

    def ejemplar_material(self, material):
        return self.filter(material=material).distinct()


class Ejemplar(TimeStampModel):
    numero_ingreso = models.CharField('Número de ingreso', max_length=50)
    codigo_barras = models.CharField('Código de barras', max_length=50)
    material = models.ForeignKey(Material)
    ubicacion = models.CharField('Ubicación', max_length=50)
    signatura = models.CharField('Signatura topográfica', max_length=60)
    precio = models.DecimalField('Precio normal en soles',max_digits=6, decimal_places=2, )
    numero_copia = models.CharField('Número de copia', max_length=20)
    archivo = models.FileField(upload_to='archivos', blank=True, null=True)
    fuente_adquisicion = models.CharField('Fuente de adquisición', max_length=60) #compra, donacion
    observacion = models.CharField('Observación', max_length=400)
    descriptores = models.ManyToManyField(Descriptor) #palabras claves
    contenido = models.TextField() #indice
    notas = models.CharField(max_length=50) #Nota general: perdido, repuesto
    descripcion_fisica = models.TextField('Descripción Física') #N° de pag, Dimensiones, Otros detalles
    prestado = models.BooleanField(default=False)
    objects = ManagerEjemplar()

    class Meta:
        verbose_name_plural = 'Ejemplares'

    def __unicode__(self):
        return self.material.titulo
