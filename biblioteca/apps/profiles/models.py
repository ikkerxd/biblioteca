from django.db import models

from apps.lector.models import Biblioteca
from django.conf import settings


class Bibliotecario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca)

    def __unicode__(self):
        return '%s' % str(self.user)
