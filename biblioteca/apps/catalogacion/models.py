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
    titulo = models.CharField(max_length=50)
    titulo_secundario = models.CharField(max_length=70, blank=True, null=True)
    tipo_material = models.ForeignKey(TipoMaterial)
    isbn = models.CharField('ISBN', max_length=50)
    sigantura = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    autor = models.ManyToManyField(Autor)
    usuario = models.FileField(settings.AUTH_USER_MODEL)
    slug = models.SlugField()
    
   ## anio_de_edicion = models.CharField(max_length=20)



    class Meta:
        verbose_name_plural = 'Materiales'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Material, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo


class KeyWord(models.Model): 
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(KeyWord, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Ejemplar(TimeStampModel):
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    numero_ingreso = models.CharField(max_length=50)
    observacion = models.CharField(max_length=400)
    prestado = models.BooleanField(default=False)
    material = models.ForeignKey(Material)
    keyword = models.ForeignKey(KeyWord)

    class Meta:
        verbose_name_plural = 'Ejemplares'

    def __unicode__(self):
        return self.material.titulo
