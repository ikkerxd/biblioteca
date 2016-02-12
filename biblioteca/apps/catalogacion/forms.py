# -*- coding: utf-8 -*- 
from django import forms
from .models import TipoMaterial
from django.forms.extras.widgets import SelectDateWidget

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

class RevisarRegistroForm(forms.Form):
	categoria = forms.ModelChoiceField(empty_label="(Seleccione una opcion)", queryset=None)
	descripcion = forms.CharField(max_length=200)
	Mostrar_desde = forms.DateField(
		widget=(
			forms.widgets.DateInput(format="%d/%m/%Y" , attrs={'class':'datepicker'})
			)
	)
	Mostrar_hasta = forms.DateField(
		widget=(
			forms.widgets.DateInput(format="%d/%m/%Y", attrs={'class':'datepicker'})
		)
	)

	def __init__(self, *args, **kwargs):
		super(RevisarRegistroForm,self).__init__(*args, **kwargs)
		self.fields['categoria'].queryset = TipoMaterial.objects.all()