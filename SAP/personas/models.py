from django.db import models


#Primero se definen las clases que no tienen relacion con otras

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    nro_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.nro_calle} {self.pais} '



# Create your models here.
class Persona(models.Model): # mdeols.Model es la clase padre va si o si
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    domicilio = models.ForeignKey(Domicilio,on_delete= models.SET_NULL, null=True) #FORENEA


    # DJANGO CREARA UNA TABLA LLAMADA PERSONA CON ESTAS COLUMNAS
    #Luego por consola: python manage.py makemigrations y crea una migracion para crear en la BD

    # se crea solo la llave foranea con id de el otro modelo, y en la BD te marca todoo

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido}, {self.email}'


