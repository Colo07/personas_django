from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    nro_personas_var = Persona.objects.count()  #accedo a la BD, object es como un manejador de la instancia, puedo extraer info del modelo
    #personas = Persona.objects.all() #regresa objetos de tipo persona
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html',{'nro_personas':nro_personas_var,'personas':personas}) #Esto es un template, pr default esta el /templates

