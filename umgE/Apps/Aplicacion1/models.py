from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    carne = models.CharField(max_length=30)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)


    def __str__(self):
	   	return  self.nombre
         #return '%s %s' % (self.nombre, self.carne)

class EstudianteAdmin(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    carne = models.CharField(max_length=30)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
        #return '%s %s' % (self.nombre, self.carne)


class Articulo(models.Model):
    titulo = models.CharField(max_length=45)
    articulo = models.CharField(max_length=300)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante)
    estudianteAdmin = models.ForeignKey(EstudianteAdmin)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
        #return '%s %s' % (self.titulo, self.estudiante)


class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante)
    articulo = models.ForeignKey(Articulo)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.fecha, self.estudiante)