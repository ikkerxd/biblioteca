from django import forms
from .models import TipoMaterial
TIPO_CHOICES = (
	 (0,"----"),
	 (1,"Titulo"),
	 (2,"Autor"),
	 (2,"Signatura"),

	)

class BusquedaForm(forms.Form):
	categoria = forms.ModelChoiceField(queryset=None)
	descripcion = forms.charfield(max_length=100)
	tipo = forms.ChoiceField(choices=TIPO_CHOICES)

	def __init__(self, *args, **kwargs):
		super(BusquedaForm,self).__init__(*args, **kwargs)
		self.fields['categoria'].queryset = TipoMaterial.object.all()

		

