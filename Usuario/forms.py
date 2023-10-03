from django import forms
from .models import *

class formUser(models.Model):
    idUser = forms.HiddenInput(required=True)
    mascota = forms
    name = forms.CharField(max_length=128, min_length=2, required=True)
    lname = forms.CharField(max_length=128, min_length=2, required=True)


