from django.shortcuts import render

def homePaseo(request):
    return render(request, 'base.html')
