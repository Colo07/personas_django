from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona

def detallePersona(request,id):
    #persona = Persona.objects.get(pk=id) #pk es primary key le indicamos q es el id
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/detalle.html',{'persona':persona})
# por defecto django tomate /templates../detalle

#PersonaForm= modelform_factory(Persona,exclude=[]) #FORMA PARA CREEAR UN OBJETO DE PERSONA PARA EL FORMULARIO



def nuevaPersona(request):
    if request.method == "POST": # si en el form se hiz un post creamos un objeto de persona con los datos del formulario y desp lo almacenamos en la bd
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save() #insert en la bd
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST": # si en el form se hiz un post creamos un objeto de persona con los datos del formulario y desp lo almacenamos en la bd
        formaPersona = PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save() #update en la bd ahora porq agarra registro existente
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index') #vuelvo hacer la peticion a la pagina inicia q tiene el metoodo de cargar todos los archivos de la bd

