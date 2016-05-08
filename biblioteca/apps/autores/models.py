from django.db import models
from django.template.defaultfilters import slugify
from apps.herencia.models import Persona
from apps.lector.models import CarreraProfesional


class TipoAutor(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo Autor'

    def __unicode__(self):
        return self.nombre


class Autor(Persona):
    Codigo = models.CharField(max_length=30, null=True, blank=True)
    carrera = models.ForeignKey(CarreraProfesional, blank=True, null=True)
    avatar = models.ImageField(upload_to='imagen_autor', blank=True, null=True)
    tipo = models.ManyToManyField(TipoAutor)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = 'Autores'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.apellidos_y_nombres)
        super(Autor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.apellidos_y_nombres
