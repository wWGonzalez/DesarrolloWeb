from __future__ import unicode_literals
from django.contrib import admin
from Apps.Aplicacion1.models import Estudiante,EstudianteAdmin,Articulo,Comentario

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(EstudianteAdmin)
admin.site.register(Articulo)
admin.site.register(Comentario)