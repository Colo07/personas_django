from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    #personalizar los atributos del formulario
    class Meta:
        model = Persona
        fields = '__all__' #q vamos a usar todos los atributos del objeto persona
        widgets = { #puedo personalizar el tipo de dato de html q va aser el atributo
            'email': EmailInput(attrs ={'type':'email'})

        }