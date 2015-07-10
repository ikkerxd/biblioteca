from django.db import models
from django.conf import settings

from apps.herencia.models import TimeStampModel
from apps.lector.models import Lector
from apps.catalogacion.models import Ejemplar


class Prestamo(TimeStampModel):
    bibliotecario = models.ForeignKey(settings.AUTH_USER_MODEL)
    lector = models.ForeignKey(Lector)
    ejemplar = models.ForeignKey(Ejemplar)
    fecha_entrega = models.DateField()

    def __unicode__(self):
        return "%s %s" % (str(self.pk), self.lector)


class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo)
    bibliotecario = models.ForeignKey(settings.AUTH_USER_MODEL)
    fecha_devolucion = models.DateField()

    class Meta:
        verbose_name_plural = 'Devoluciones'
