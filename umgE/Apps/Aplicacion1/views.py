

from __future__ import unicode_literals
#from django.views.generic.edit import FormView


from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import EstudianteForm,EstudianteAdminForm,ArticuloForm,ComentarioForm
from .models import Estudiante,EstudianteAdmin,Articulo,Comentario

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect

def EstudianteList(request):
	obj = Estudiante.objects.all()
	for entrada in obj:
		obj_nombre = entrada.nombre
		obj_direccion = entrada.direccion
		obj_carne = entrada.carne

	context = {
	"obj":   obj,
	"obj_nombre":obj_nombre,
	"obj_direccion":obj_direccion,
	"obj_carne":obj_carne,

	}
	return render(request,"Estudiante_listar.html",context)


def EstudianteListAdmin(request):
	obj = EstudianteAdmin.objects.all()
	for entrada in obj:
		obj_nombre = entrada.nombre
		obj_direccion = entrada.direccion
		obj_carne = entrada.carne

	context = {
	"obj":   obj,
	"obj_nombre":obj_nombre,
	"obj_direccion":obj_direccion,
	"obj_carne":obj_carne,

	}
	return render(request,"EstudianteAdmin_listar.html",context)




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
	success_url = reverse_lazy('App1:home')


class ComentarioView(CreateView):
	template_name = 'Comentario.html'
	form_class = ComentarioForm
	success_url = reverse_lazy('App1:home')