from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from apps.herencia.models import TimeStampModel
from apps.autores.models import Autor


class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Tipo de Material'

    def __unicode__(self):
        return self.nombre


class Material(TimeStampModel):
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    titulo = models.CharField(max_length=50)
    titulo_secundario = models.CharField(max_length=70, blank=True, null=True)
    tipo_material = models.ForeignKey(TipoMaterial, blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=50, blank=True, null=True)
    signatura = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor)
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
    numero_ingreso = models.CharField(max_length=50)
    observacion = models.CharField(max_length=400)
    prestado = models.BooleanField(default=False)
    material = models.ForeignKey(Material)
    descriptores = models.ManyToManyField(Descriptor)
    pais = models.CharField('lugar de edicion', max_length=50)
    editorial = models.CharField(max_length=70)
    descripcion_fisica = models.TextField()
    dimensiones = models.TextField()
    notas = models.CharField(max_length=50)
    contenido = models.TextField()
    archivo = models.FileField(upload_to='archivos')

    objects = ManagerEjemplar()

    class Meta:
        verbose_name_plural = 'Ejemplares'

    def __unicode__(self):
        return self.material.titulo
