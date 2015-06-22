from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class meta:
        abstract = True


SEXO_CHOICES = (
    ('M', 'masculino'),
    ('F', 'femenino'),
)


class Persona(TimeStampModel):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class meta:
        abstract = True
