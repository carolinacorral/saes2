from django.db import models

class Alumno(models.Model):
    boleta = models.CharField(max_length=10, primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    edad = models.IntegerField()
    foto_perfil = models.URLField()
    parcial1 = models.FloatField()
    parcial2 = models.FloatField()
    parcial3 = models.FloatField()
    final = models.FloatField()

class Gestion(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    foto_perfil = models.URLField()
