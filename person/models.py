from django.db import models
from enum import Enum
# from pet.models import Pet
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class MonthEnum(Enum):
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

class Locality(models.Model):
    idLocality = models.PositiveSmallIntegerField(primary_key=True)
    locality = models.CharField(max_length=128, blank=False, null=False)

class Person(AbstractUser):
    idPerson=models.PositiveIntegerField(primary_key=True)
    idLocality=models.ForeignKey(Locality, on_delete=models.DO_NOTHING)
    username = models.CharField(blank=False, null=False, db_column='phone', unique=True, max_length=15)#Renaming username as phone
    is_staff = models.BooleanField(default = False, db_column='isClient')
    isAdmin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False, db_column='active')
    email = models.CharField(null=False, blank=False)
    class Meta:
            ordering = ['last_name', 'first_name']
            # unique_together = ['idPerson', 'idPet']
            # constraints = [
            #     models.UniqueConstraint(fields=['idPerson', 'idPet'], name='const_person_together')
            # ]

class Interview(models.Model):
    idInterview=models.PositiveIntegerField(primary_key=True)
    idPerson=models.ForeignKey(Person, on_delete=models.DO_NOTHING, )
    date=models.DateTimeField(blank=False, null=False)
    quotas=models.PositiveSmallIntegerField(default=0)
    # time=models.CharField(max_length=64, blank=False, null=False)
    
# class dayCare(models.Model):
#     idDayCare = models.PositiveIntegerField(primary_key=True)
#     idPerson = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
#     idPet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
#     idLocality = models.ForeignKey(Locality, on_delete=models.DO_NOTHING)
#     date = models.DateTimeField(blank=False, null=False, default= timezone.now().day)
#     price = models.PositiveIntegerField(blank=False, null=False) #DecimalField(max_digits=6, decimal_places=2) for numeric fields
#     quotas = models.PositiveSmallIntegerField(blank=False, null=False)
    
    


