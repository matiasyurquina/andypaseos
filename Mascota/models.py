from django.db import models
from enum import Enum

class Nivel_soc(Enum):
    B = 'Bajo'
    M = 'Medio'
    A = 'Alto'

class Raza(models.Model):
    idRaza = models.PositiveIntegerField(primary_key=True)
    raza = models.CharField(max_length=128)

class Mascota(models.Model):
    idMascota = models.PositiveIntegerField(primary_key=True, unique=True)
    raza = models.ForeignKey(Raza, on_delete=models.DO_NOTHING, unique=True)
    puro = models.BooleanField(default=True)
    nombre = models.CharField(max_length=128)
    sexo = models.BooleanField()#false = hembra; true = macho
    fecha_nac = models.DateField()
    castrado = models.BooleanField()
    nivel_soc = models.PositiveSmallIntegerField(default=0)# de 0 a 2, B, M y A
    obs = models.CharField(max_length=128)

class Meta:
    ordering = ['fecha_paseo']
    unique_together = ['idMascota', 'raza']
    constraints = [
             models.UniqueConstraint(fields=['idMascota', 'raza'], name='const_mascota_together')
    ]
