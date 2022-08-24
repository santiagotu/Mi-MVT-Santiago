from django.shortcuts import render
from .models import Familiar

# Create your views here.

#def familiares(request):

    #familiar = Familiar.objects.create(nombre = "David",edad = 70, fecha_nacimiento = "1952-01-04")

    #context = {'familiar': familiar}

    #return render(request, "familiares.html", context)#

def ver_familiares(request):
    familiares = Familiar.objects.all()
    context = {'familiares': familiares}
    return render(request, "familiares.html", context)




