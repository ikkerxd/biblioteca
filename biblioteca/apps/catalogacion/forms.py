# -*- coding: utf-8 -*- 
from django import forms
from .models import TipoMaterial
TIPO_CHOICES = (
	 (0,"seleccione una opcion"),
	 ('titulo',"Titulo"),
	 ('autor',"Autor"),
	 ('signatura',"Signatura Topográfica"),

	)

class BusquedaForm(forms.Form):
	categoria = forms.ModelChoiceField(queryset=None)
	descripcion = forms.CharField(max_length=100)
	tipo = forms.ChoiceField(choices=TIPO_CHOICES)

	def __init__(self, *args, **kwargs):
		super(BusquedaForm,self).__init__(*args, **kwargs)
		self.fields['categoria'].queryset = TipoMaterial.objects.all()


		

