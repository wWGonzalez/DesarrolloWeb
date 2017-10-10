

from __future__ import unicode_literals
#from django.views.generic.edit import FormView



from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import EstudianteForm,EstudianteAdminForm,ArticuloForm,ComentarioForm
from .models import Estudiante,EstudianteAdmin,Articulo,Comentario

from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect



def EstudianteList(request):
	estudiantes = Estudiante.objects.all()
	context = {'estudiantes':estudiantes}
	return render(request,"Estudiante_listar.html",context)

#def EstudianteList(request):
#	obj = Estudiante.objects.all()
#	for entrada in obj:
#		obj_nombre = entrada.nombre
#		obj_direccion = entrada.direccion
#		obj_carne = entrada.carne

#	context = {
#	"obj":   obj,
#	"obj_nombre":obj_nombre,
#	"obj_direccion":obj_direccion,
#	"obj_carne":obj_carne,

#	}
#	return render(request,"Estudiante_listar.html",context)


def EstudianteListAdmin(request):
	obj = EstudianteAdmin.objects.all()
	context = {'obj':obj}
	return render(request,"EstudianteAdmin_listar.html",context)


def ArticuloList(request):
	articulos = Articulo.objects.all()
	context = {'articulos':articulos}
	return render(request,"Articulo_List.html",context)



# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'

class EstudianteView(TemplateView):
	template_name='Estudiante.html'

class AdministradoresView(TemplateView):
	template_name='Administradores.html'

class AcercaDeView(TemplateView):
	template_name='AcercaDe.html'

class LoginView(FormView):
	template_name='login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('App1:home')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)


def logout_view(request):
	logout(request)
	return redirect('App1:home')








#class CrearEstudianteView(CreateView):
#template_name = 'crearEstudiante.html'
#form_class = EstudianteForm
#success_url = reverse_lazy('App1:home')

class crearEstudianteView(CreateView):
	template_name = 'crearEstudiante.html'
	form_class = EstudianteForm
	success_url = reverse_lazy('App1:home')






class crearEstudainteAdminView(CreateView):
	template_name = 'crearEstudianteAdmin.html'
	form_class = EstudianteAdminForm
	success_url = reverse_lazy('App1:home')


class ArticuloView(CreateView):
	template_name = 'Articulo.html'
	form_class = ArticuloForm
	success_url = reverse_lazy('App1:ArticuloList')


class ComentarioView(CreateView):
	template_name = 'Comentario.html'
	form_class = ComentarioForm
	success_url = reverse_lazy('App1:home')





	#Vistas para Editar
class EditarEstudianteView(UpdateView):
	template_name = 'crearEstudiante.html'
	model = Estudiante
	form_class = EstudianteForm
	success_url = reverse_lazy('App1:EstudianteList')

class EditarEstudianteAdminView(UpdateView):
	template_name = 'crearEstudianteAdmin.html'
	model = EstudianteAdmin
	form_class = EstudianteAdminForm
	success_url = reverse_lazy('App1:EstudianteListAdmin')

class EditarArticuloView(UpdateView):
	template_name = 'Articulo.html'
	model = Articulo
	form_class = ArticuloForm
	success_url = reverse_lazy('App1:ArticuloList')


	#Vistaas para eliminar
class EliminarEstudianteView(DeleteView):
	template_name = 'Eliminar.html'
	model = Estudiante
	success_url = reverse_lazy('App1:EstudianteList')

class EliminarEstudianteAdminView(DeleteView):
	template_name = 'Eliminar.html'
	model = EstudianteAdmin
	success_url = reverse_lazy('App1:EstudianteListAdmin')

class EliminarArticuloView(DeleteView):
	template_name = 'Eliminar.html'
	model = Articulo
	success_url = reverse_lazy('App1:ArticuloList')