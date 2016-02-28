# -*- coding: utf-8 -*- 
from django import forms
from .models import TipoMaterial
from django.forms.widgets import Select
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape


TIPO_CHOICES = (
	 ('Catalogo de Biblioteca', {'label':'Catalogo de Biblioteca', 'disabled selected':True}), 
	 ('titulo',"Titulo"),
	 ('autor',"Autor"),
	 ('signatura',"Signatura Topográfica"),
	)

class SelectWithDisabled(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    To disable an option, pass a dict instead of a string for its label,
    of the form: {'label': 'option label', 'disabled': True}
    """
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if (option_value in selected_choices):
            selected_html = u' selected="selected"'
        else:
            selected_html = ''
        disabled_html = ''
        if isinstance(option_label, dict):
            if dict.get(option_label, 'disabled selected'):
                disabled_html = u' disabled selected="disabled selected"'
            option_label = option_label['label']
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, disabled_html,
            conditional_escape(force_unicode(option_label)))

class BusquedaForm(forms.Form):
	categoria = forms.ModelChoiceField(empty_label="Seleccione una categoría",queryset=None)
	descripcion = forms.CharField(max_length=100,
		widget=(
				forms.widgets.TextInput(attrs={'placeholder': 'Introduzca la búsqueda','required': True})
				)
	)
	#tipo = forms.ChoiceField(choices=TIPO_CHOICES)
	tipo =forms.ChoiceField(choices=TIPO_CHOICES, widget=SelectWithDisabled())
	#tipo= forms.ChoiceField(choices=TIPO_CHOICES, widget=(forms.widgets.Select(attrs={'required': True, 'disabled':'Catálogo de Biblioteca'})))

	def __init__(self, *args, **kwargs):
		super(BusquedaForm,self).__init__(*args, **kwargs)
		self.fields['categoria'].queryset = TipoMaterial.objects.all()

class RevisarRegistroForm(forms.Form):
	categoria = forms.ModelChoiceField(empty_label="Seleccione una categoría", queryset=None)
	descripcion = forms.CharField(max_length=100,
		widget=(
				forms.widgets.TextInput(attrs={'placeholder': 'Introduzca la búsqueda','required': True})
				)
	)
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

