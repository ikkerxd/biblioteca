from django.db import models
from django.conf import settings

from apps.herencia.models import TimeStampModel
from apps.lector.models import Lector, Biblioteca
from apps.catalogacion.models import Ejemplar


class Prestamo(TimeStampModel):
    bibliotecario = models.ForeignKey(settings.AUTH_USER_MODEL , editable=False)
    lector = models.ForeignKey(Lector)
    ejemplar = models.ForeignKey(Ejemplar)
    fecha_entrega = models.DateField()
    devuelto = models.BooleanField(default=False)
    #la ubicacion lo obtendremos de la ubicacion del ejemplar
    #biblioteca = models.ForeignKey(Biblioteca, blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (str(self.pk), self.lector)


class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo)
    bibliotecario = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    fecha_devolucion = models.DateField()

    class Meta:
        verbose_name_plural = 'Devoluciones'


class Semestre(models.Model):
    nombre = models.CharField(max_length=10) #ejemplo: 2016-1
    inicio_semestre = models.DateField()
    fin_semestre = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Semestre, self).save(*args, **kwargs)
