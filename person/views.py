from django.shortcuts import render, redirect
from django.db.utils import IntegrityError, InternalError
from django.contrib.auth import authenticate, login, logout


from person.models import *

def getPerson(idPerson:int)->Person: #GETs person by ID if exists
    try:
        p = Person.objects.get(pk=idPerson)
        return p 
    except:
        return None

def save_person(req)->int:
    b=-1 #Error
    try:
        idPerson=Person.objects.all().__len__()+1
        name = str.upper(req['name'])
        lname = str.upper(req['lname'])
        mail = str.lower(req['mail'])
        phone = req['cel']
        passwd = req['pass']
        idLocality = Locality.objects.get(pk=req['locality'])

        p = Person.objects.create_user(phone, mail, passwd, idLocality=idLocality, idPerson=idPerson, first_name=name, last_name=lname)
        p.save()
        b=0#correct!
    except IntegrityError:
        b=1
        return b#integrity error 
    except Exception as e:
        b=-1
        return b 
    
def update_person(req)->int:
    b=-1 #Error
    print(req)
    print(len(req['pass'].strip()))
    
    try:
        
        idPerson = req['idPerson']
        p=Person.objects.get(pk=idPerson)
        name = str.upper(req['name'])
        lname = str.upper(req['lname'])
        idLocality = Locality.objects.get(pk=req['locality'])

        if len(req['pass'].strip())>1:
            passwd = req['pass']
            p.password=passwd

        p.first_name=name
        p.last_name=lname
        p.idLocality=idLocality
        p.save()
        b=0#correct!
    except IntegrityError:
        b=1
        return b#integrity error 
    except Exception as e:
        b=-1
        return b 

def signup(request):
    
    if request.POST: #if submit
        req=save_person(request.POST)
        if req==0:
            return render(request, 'signup/success.html')
        elif req==1:#INTEGRITY ERROR
            error = "El correo o teléfono ingresado ya se encuentra registrado"
            return render(request, 'signup/error.html', {'error': error})
        else:#ANY OTHER CATCHED ERROR
            error = 'Ocurrió un error inesperado'
            return render(request, 'signup/error.html', {'error': error})
    else:#if not
        locality=Locality.objects.all()
        return render(request, 'signup/index.html', {'locality': locality})
    
def myAccount(request):

    if request.POST:
        req=update_person(request.POST)
        p = getPerson(request.POST['idPerson'])
        if req==0:#success
            print(request.POST)
            return render(request, 'login/myAccount.html', {'user': p})
        elif req==1:
            return render(request, 'login/myAccount.html', {'user': p})
        else:
            return render(request, 'login/myAccount.html', {'user': p})
        
    else:
        p = getPerson(1)
        return render(request, 'login/myAccount.html', {'user': p})     


def login(request):
    return render(request, 'login/login.html')

def login_view(request):
    # try: 
        # user = Person.objects.create_user('matiasyurquina', 'matias_cx@yahoo.com.ar', 'G2220HDA')
        # user.first_name = 'Matias'
        # user.last_name = 'Yurquina'
        # user.is_superuser = True
        # user.is_staff = True
        # user.email = 'matias_cx@yahoo.com.ar'
        # user.save()
        # print("Se creó correctamente")
    # except:
    #     print("asdasad")
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request)
                return redirect('dayCare')
        return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')