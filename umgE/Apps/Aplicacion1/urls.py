

from django.conf.urls import url,include
from .views import IndexView,EstudianteView,EstudianteList,EstudianteListAdmin,AdministradoresView,AcercaDeView,crearEstudianteView,crearEstudainteAdminView,LoginView,logout_view,ArticuloView,ComentarioView
#from django.contrib.auth import views as auth_views

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
	url(r'^logout$', logout_view,name='logout'),

	#url(r'^logout/$', auth_views.logout, {'next_page': 'App1:home'}, name='logout'),

	url(r'^Articulo$', ArticuloView.as_view(),name='Articulo'),
	url(r'^Comentario$', ComentarioView.as_view(),name='Comentario'),



	

]