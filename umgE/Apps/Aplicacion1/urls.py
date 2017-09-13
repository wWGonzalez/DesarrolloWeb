

from django.conf.urls import url,include
from .views import IndexView,EstudianteView,EstudianteList,EstudianteListAdmin,AdministradoresView,AcercaDeView,crearEstudianteView,crearEstudainteAdminView,LoginView,ArticuloView,ComentarioView


urlpatterns = [
	url(r'^$', IndexView.as_view(),name='home'),
	url(r'^Estudiante$', EstudianteView.as_view(),name='Estudiante'),
	url(r'^EstudianteList$', EstudianteList,name='EstudianteList'),
	url(r'^EstudianteListAdmin$', EstudianteListAdmin,name='EstudianteListAdmin'),


	url(r'^Administradores$', AdministradoresView.as_view(),name='Administradores'),
	url(r'^AcercaDe$', AcercaDeView.as_view(),name='AcercaDe'),
	url(r'^AddEstudiante$', crearEstudianteView.as_view(),name='addEstudiante'),
	url(r'^AddEstudianteAdmin$', crearEstudainteAdminView.as_view(),name='AddEstudianteAdmin'),
	url(r'^login$', LoginView.as_view(),name='login'),

	url(r'^Articulo$', ArticuloView.as_view(),name='Articulo'),
	url(r'^Comentario$', ComentarioView.as_view(),name='Comentario'),

	

]