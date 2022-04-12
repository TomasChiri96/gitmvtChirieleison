from django.db import models
from datetime import date, time

# Create your models here.

class familiar(models.Model):

    nombre = models.CharField('nombre',max_length=70)
    apellido = models.CharField('apellido',max_length=70)
    edad = models.IntegerField('edad')
    fecha_nacimiento = models.DateField('fecha de nacimiento', auto_now = True)

class mascota(models.Model):
    
    raza = models.CharField(max_length=50)
    nombre = models.CharField('nombre', max_length=20)
