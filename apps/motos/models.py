from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    foto  = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)
    cedula = models.IntegerField(unique=True)
    telefono = models.IntegerField(null=True, blank=True)
    dirección = models. CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres + " " + self.apellidos
    
class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cilindraje = models.IntegerField()
    foto_moto = models.ImageField(upload_to='fotos_motos', null=True, blank=True)
    color = models.CharField(max_length=100)
    placa = models.CharField(unique=True, max_length=100) 
    chasis = models.CharField(unique=True, max_length=100)
    
    def __str__(self):
        return self.marca + " " + self.modelo
estados=(
    ('Vendida', 'Vendida'),
    ('Siniestro', 'Siniestro'),
    ('Pendiente', 'Pendiente'),
    ('En propiedad', 'En propiedad'),

)

class Historial(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.PROTECT)
    propietario = models.ForeignKey(Persona, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices= estados, default='En propiedad') 

    def __str__(self):
        return str(self.moto) + " " + self.estado 


class  Mantenimientos(models.Model):
    nombres = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    descripción = models.TextField(null=True, blank=True)
    id_historial = models.ForeignKey(Historial, on_delete=models.PROTECT)