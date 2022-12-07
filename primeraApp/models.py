from django.db import models

class Videojuegos(models.Model):
    nombre = models.CharField(max_length=50)
    desarrollador = models.CharField(max_length=50)
    generos = models.CharField(max_length=50)
    plataformas = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    puntuacion = models.CharField(max_length=2, default='')