from django.shortcuts import render

def registro(request):    
    return render(request, 'Usuario/index.html')
