from django.db import models
from enum import Enum
from django.utils import timezone
from person.models import Person
from person.models import Locality

class socLevel(models.TextChoices):
    B = 'Low'
    M = 'Medium'
    A = 'High'

class Race(models.Model):
    idRace = models.PositiveIntegerField(primary_key=True)
    race = models.CharField(max_length=64)

class Pet(models.Model):
    idPet = models.PositiveIntegerField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    idRace = models.ForeignKey(Race, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    birth = models.DateField(blank=False, null=False)
    pure = models.BooleanField(default=True)
    gender = models.BooleanField()#false = hembra; true = macho
    castrated = models.BooleanField()
    socLevel = models.CharField(max_length=6, blank=False, null=False, choices=socLevel.choices, default=socLevel.A)# de 0 a 2, B, M y A
    obs = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        unique_together = ['idPerson', 'name']
        constraints = [
                models.UniqueConstraint(fields=['idPerson', 'name'], name='const_pet_distinct')
                ]
        
class dayCare(models.Model):
    idDayCare = models.PositiveIntegerField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    idPet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False) #DecimalField(max_digits=6, decimal_places=2) for numeric fields
    quotas = models.PositiveSmallIntegerField(blank=False, null=False)

    class Meta:
        ordering = ['date']
        unique_together = ['idDayCare', 'idPerson', 'idPet', 'date']
        constraints = [
                models.UniqueConstraint(fields=['idDayCare', 'idPerson', 'idPet', 'date'], name='const_dayCare_distinct')
        ]
    

class Ride(models.Model):
    idRide = models.PositiveIntegerField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    idPet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False) #DecimalField(max_digits=6, decimal_places=2) for numeric fields
    quotas = models.PositiveSmallIntegerField(blank=False, null=False)

    class Meta:
        ordering = ['date']
        unique_together = ['idRide', 'idPerson', 'idPet', 'date']
        constraints = [
                models.UniqueConstraint(fields=['idRide', 'idPerson', 'idPet', 'date'], name='const_ride_distinct')
        ]



