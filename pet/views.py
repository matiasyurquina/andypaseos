from django.shortcuts import render
from pet.models import * 
from person.views import getPerson
import datetime
import os
import sweetify

_idPerson=1

_public_races = Race.objects.all()

def getRaces():
    return _public_races

def getMyPets(idPerson):
    p = Pet.objects.filter(idPerson=idPerson).order_by('name')
    return p


def newPet(req)->bool:
    
    # try:
        idPet = Pet.objects.all().__len__()+1
        newPet=Pet()
        newPet.idPet = idPet
        newPet.name = req['name']
        newPet.birth = req['birth']
        newPet.idRace =  Race.objects.get(pk=req['idRace'])
        newPet.idPerson =  getPerson(1) #req['idPerson'] es el valor, pero lo hardcodee por 1
        if req['pure']==True:
            newPet.pure=True
        else:
            newPet.pure=False
        
        if req['gender']==True:
            newPet.gender=True
        else:
            newPet.gender=False

        if req['castrated']==True:
            newPet.castrated=True
        else:
            newPet.castrated=False

        newPet.socLevel=req['socLevel']

        newPet.save()
    # except:
    #     return False
    # return True


def myPets(request):
    if request.POST:
        
        if newPet(request.POST):
            msg = "Se guardó correctamente"
        else: 
            msg = "Ocurrió un error"
        return render(request, 'myPets/index.html', {'races':getRaces(), 'msg': msg, 'myPets': getMyPets(1)})        #HARDCODEADO EN 1, CAMBIAR POR el username de la sesion
    else:
        return render(request, 'myPets/index.html', {'races':getRaces(), 'myPets': getMyPets(1) }) 

def ride(request):
    rides = check_available_rides()
    if request.POST:
        id=request.POST['rides']
        # r = Ride.objects.get(pk=id)
        if newRide(id, 1, 1, '07-06-2024')==0:
            
        else:

        myRides=0


        return render(request, 'ride/index.html', {'av_rides': rides, 'myRides':myRides})
    else:
        #available rides
        return render(request, 'ride/index.html', {'av_rides': rides})
    
def getRideHistory(request):
    
    if request.POST:
        idPerson=request.POST['idPerson']
        history = Ride.objects.all().filter(idPerson=idPerson)
        return render(request, 'ride/index.html', {'history': history})
    return render(request, 'ride/index.html')

def dayCare(request):
    return render(request, 'dayCare/index.html')

def getRideHistory(request):
    
    if request.POST:
        idPerson=request.POST['idPerson']
        history = dayCare.objects.all().filter(idPerson=idPerson)
        return render(request, 'dayCare/index.html', {'history': history})
    return render(request, 'dayCare/index.html')

def check_available_rides():
    
#   rides = Ride.objects.filter(date__lt=datetime.datetime.now())
    rides = Ride.objects.all().filter(quotas__gt=1 ) #add DATE filter 
    return rides

def newRide(idRide, idPerson, idPet, date):

    try:
        r = Ride.objects.get(pk=idRide)
        r.idPerson=idPerson
        r.idPet=idPet
        r.date = date
        r.price = price
        if r.quotas >=1:
            r.quotas = r.quotas-1
            r.save()
            return 0
        else:
            return 1
    except:
        return 1


# fecha_sorteo__gte = datetime.now().strftime('%Y-%m-%d')