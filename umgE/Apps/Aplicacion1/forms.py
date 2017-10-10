from django import forms
from .models import Estudiante,EstudianteAdmin,Articulo,Comentario

class EstudianteForm(forms.ModelForm):
	 class Meta:
	 	model = Estudiante
	 	fields = '__all__'


	 	
class EstudianteAdminForm(forms.ModelForm):
	 class Meta:
	 	model = EstudianteAdmin

	 	fields = '__all__'

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		fields = [
		'titulo',
		'articulo',
		'fecha',
		'estudiante',
		'estudianteAdmin',
				]

		widgets = {
            'articulo': forms.Textarea(attrs={'cols': 24, 'rows': 6}),
        }




class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = '__all__'