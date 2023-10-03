from django.db import models
from enum import Enum
from Mascota.models import Mascota

class MesEnum(Enum):
  Ene = 'Enero'
  Feb = 'Febrero'
  Mar = 'Marzo'
  Abr = 'Abril'
  May = 'Mayo'
  Jun = 'Junio'
  Jul = 'Julio'
  Ago = 'Agosto'
  Sep = 'Septiembre'
  Oct = 'Octubre'
  Nov = 'Noviembre'
  Dic = 'Diciembre'

class Localidad(models.Model):
    idLocalidad = models.PositiveSmallIntegerField(primary_key=True)
    localidad = models.CharField(max_length=128)

class Usuario(models.Model):
    idUser=models.PositiveIntegerField(primary_key=True)
    mascota=models.ForeignKey(Mascota, on_delete=models.DO_NOTHING)
    localidad=models.ForeignKey(Localidad, on_delete=models.DO_NOTHING)

    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    fecha_nac=models.DateField()
    cel=models.BigIntegerField(blank=False, null=False)
    dir = models.CharField(max_length=128)
    email = models.EmailField(blank=False, null=False)
    habilitado = models.BooleanField(default=False)
    
class Meta:
        ordering = ['apellido', 'nombre']
        unique_together = ['idUser', 'mascota']
        constraints = [
            models.UniqueConstraint(fields=['idUser', 'mascota'], name='const_User_together')
        ]


    
