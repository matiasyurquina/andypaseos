from django.contrib import admin
from django.urls import path
from django.conf import settings
from andypaseos import views
from Usuario import views as uViews
from Mascota import views as mViews
from Paseo import views as pViews
from Guarderia import views as gViews

urlpatterns = [
    path('', views.home),
    path('registro', uViews.registro),
    #path('mascota/', uViews.registro)

]
