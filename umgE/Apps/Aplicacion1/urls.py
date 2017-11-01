

from django.conf.urls import url,include
from .views import EstudianteAdminListView,EliminarArticuloView,EliminarEstudianteAdminView,ArticuloList,EliminarEstudianteView,EditarArticuloView,EditarEstudianteAdminView,EstudianteList,EstudianteListAdmin,IndexView,EstudianteView,AdministradoresView,AcercaDeView,crearEstudianteView,crearEstudainteAdminView,LoginView,logout_view,ArticuloView,ComentarioView,EditarEstudianteView
from .views import EstudianteListView
#from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', IndexView.as_view(),name='home'),
	url(r'^Estudiante$', EstudianteView.as_view(),name='Estudiante'),
	url(r'^ArticuloList$', ArticuloList,name='ArticuloList'),
	url(r'^EstudianteList$', EstudianteListView.as_view(),name='EstudianteList'),
	url(r'^EstudianteListAdmin$', EstudianteAdminListView.as_view(),name='EstudianteListAdmin'),



	url(r'^Administradores$', AdministradoresView.as_view(),name='Administradores'),
	url(r'^AcercaDe$', AcercaDeView.as_view(),name='AcercaDe'),
	url(r'^AddEstudiante$', crearEstudianteView.as_view(),name='addEstudiante'),
	url(r'^AddEstudianteAdmin$', crearEstudainteAdminView.as_view(),name='AddEstudianteAdmin'),
	url(r'^login$', LoginView.as_view(),name='login'),
	url(r'^logout$', logout_view,name='logout'),


	#url(r'^logout/$', auth_views.logout, {'next_page': 'App1:home'}, name='logout'),


	url(r'^EliminarEstudiante/(?P<pk>\d+)/$', EliminarEstudianteView.as_view(), name='DeleteEstudiante'),
	url(r'^EliminarEstudianteAdmin/(?P<pk>\d+)/$', EliminarEstudianteAdminView.as_view(), name='DeleteAdmin'),
	url(r'^EliminarArticuloAdmin/(?P<pk>\d+)/$', EliminarArticuloView.as_view(), name='DeleteArticulo'),

	url(r'^EditarArticulo/(?P<pk>\d+)/$', EditarArticuloView.as_view(), name='EditarArticulo'),
	url(r'^EditarEstudianteAdmin/(?P<pk>\d+)/', EditarEstudianteAdminView.as_view(), name='EditarEstudianteAdmin'),
	url(r'^EditarEstudiante/(?P<pk>\d+)/$', EditarEstudianteView.as_view(), name='EditarEstudiante'),
	url(r'^Articulo$', ArticuloView.as_view(),name='Articulo'),
	url(r'^Comentario$', ComentarioView.as_view(),name='Comentario'),



	

]