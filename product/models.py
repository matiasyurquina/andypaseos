from django.db import models
from person.models import Person
from django.utils import timezone

class Product(models.Model):
    idProduct=models.PositiveIntegerField(primary_key=True)
    picture=models.ImageField(blank=False, null=False)
    category=models.CharField(max_length = 32, blank=False, null=False)
    product=models.CharField(max_length = 32, blank=False, null=False)
    stock = models.PositiveSmallIntegerField(default = 0, blank = False, null=False)
    description = models.CharField(blank=False, null=False, max_length=512)
    available = models.BooleanField(default=False)


class Selling(models.Model):
    idSelling=models.PositiveIntegerField(primary_key=True)
    idProduct=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    idPerson=models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    product=models.CharField(max_length = 32, blank=False, null=False)
    date=models.DateTimeField(blank=False, null=False, default= timezone.now().day)
    quantity=models.PositiveSmallIntegerField(default=1, blank=False, null=False)
