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
    apellidos_y_nombres = models.CharField(max_length=160)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class meta:
        abstract = True
