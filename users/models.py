from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Encuesta(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    consulta = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechapub = models.DateTimeField(default=timezone.now)
    fechamax = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.consulta

class Informe(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechapub = models.DateTimeField(default=timezone.now)
    foto = models.CharField(max_length=200)
    def __str__(self):
        return self.titulo
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechapub = models.DateTimeField(default=timezone.now)
    fecha_realizara = models.DateTimeField(default=timezone.now)
    foto = models.CharField(max_length=200)
    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    encuesta = models.ForeignKey('Encuesta',default=1,on_delete=models.SET_DEFAULT)
    RESPUESTA = (
        ('SI','SI'),
        ('NO','NO'),
    )
    respuesta = models.CharField(max_length=80,choices=RESPUESTA,default='DISPONIBLE')
    def __str__(self):
        return self.respuesta

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username