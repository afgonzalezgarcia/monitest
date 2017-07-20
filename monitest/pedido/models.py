from __future__ import unicode_literals
from django.core.validators import MinValueValidator

from django.db import models

# Create your models here.

class Pedido(models.Model):
    dni = models.CharField(max_length=15)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    amount = models.FloatField(default=1.0, validators=[MinValueValidator(1)])
    status = models.CharField(max_length=150,blank=True, null=True)
    email = models.EmailField(max_length=100)

    #
    masculino = 'Masculino'
    femenino = 'Femenino'
    GENDER_CHOICES = (
        (masculino, 'M'),
        (femenino, 'F'),
    )
    gender = models.CharField(max_length=15,
                              choices=GENDER_CHOICES,
                              default=masculino)
    #

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
