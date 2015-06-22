from django.db import models
from django.template.defaultfilters import slugify
from apps.herencia.models import Persona


class CarreraProfesional(models.Model):
    codigo = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = 'Carreras Profesionales'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(CarreraProfesional, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class TipoLector(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo Lector'

    def __unicode__(self):
        return self.nombre


class Lector(Persona):
    Codigo = models.CharField(max_length=30, unique=True)
    carrera = models.ForeignKey(CarreraProfesional, blank=True, null=True)
    dni = models.CharField(max_length=8)
    avatar = models.ImageField(upload_to='imagen_lector', blank=True, null=True)
    estado = models.BooleanField()
    tipo = models.ForeignKey(TipoLector)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = 'Lectores'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify("%s %s" % (self.nombres, self.apellidos))
        super(Lector, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s" % (self.nombres, self.apellidos)
