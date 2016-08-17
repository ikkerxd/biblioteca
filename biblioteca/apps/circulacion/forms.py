# -*- encoding: utf-8 -*-

from django import forms
from .models import Prestamo

from apps.lector.models import Lector,TipoLector,Biblioteca
from apps.catalogacion.models import Ejemplar

from datetime import date


class LectorPrestamoForm(forms.Form):
    lector = forms.CharField(
        label='número de carnet',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )

    def clean(self):
        cleaned_data = super(LectorPrestamoForm, self).clean()
        codigo = cleaned_data.get('lector')

        existe_lector = Lector.objects.filter(codigo=codigo).exists()
        if not existe_lector:
            mensaje = 'El lector no esta registrado'
            raise forms.ValidationError(mensaje)
        else:
            lector = Lector.objects.get(codigo=codigo)
            if not lector.fecha_inicio or not lector.fecha_fin:
                mensaje = 'El lector no se encuentra matriculado en el semestre'
                raise forms.ValidationError(mensaje)
            hoy = date.today();
            # verficamos el rango de fechas
            if not (lector.fecha_inicio < hoy and hoy < lector.fecha_fin):
                mensaje = 'El carnet del lector a caducado.'
                raise forms.ValidationError(mensaje)

        return cleaned_data


class LibroPrestamoForm(forms.Form):
    codigo = forms.CharField(
        label='codigo de barras',
        widget=forms.TextInput(
            attrs={'class': 'validate', 'placeholder': 'Ingrese codigo de barras'}
        ),
    )

    def clean(self):
        cleaned_data = super(LibroPrestamoForm, self).clean()
        codigo = cleaned_data.get('codigo')
        existe_codigo = Ejemplar.objects.filter(codigo_barras=codigo).exists()
        if not existe_codigo:
            mensaje = 'el item no esta registrado'
            raise forms.ValidationError(mensaje)
        else:
            ejemplar = Ejemplar.objects.get(codigo_barras=codigo)
            prestado = ejemplar.prestado
            print prestado
            if prestado:
                mensaje = "El item se encuentra prestado"
                raise forms.ValidationError(mensaje)
        return cleaned_data


class DevolucionForm(forms.Form):
    codigo = forms.CharField(
        label='codigo de barras',
        widget=forms.TextInput(
            attrs={'class': 'validate', 'placeholder': 'Ingrese codigo de barras'}
        ),
    )

    def clean(self):
        cleaned_data = super(DevolucionForm, self).clean()
        codigo = cleaned_data.get('codigo')
        prestamo = Prestamo.objects.filter(ejemplar__codigo_barras=codigo)
        if not prestamo.exists():
            print '1 error'
            mensaje = 'El ejemplar no existe'
            raise forms.ValidationError(mensaje)
        elif not prestamo[0].ejemplar.prestado:
            print '2 error'
            mensaje = 'El ejemplar no se encuentra prestado'
            raise forms.ValidationError(mensaje)
        return cleaned_data

class DeudoresForm(forms.Form):
    tipo_lector = forms.ModelChoiceField(empty_label="(Seleccione tipo de lector)",queryset=None)
    biblioteca = forms.ModelChoiceField(empty_label="(todos)",queryset=None,required=False)

    def __init__(self, *args, **kwargs):
        super(DeudoresForm,self).__init__(*args, **kwargs)
        self.fields['tipo_lector'].queryset = TipoLector.objects.all().order_by('nombre')
        self.fields['biblioteca'].queryset = Biblioteca.objects.all().order_by('nombre')
