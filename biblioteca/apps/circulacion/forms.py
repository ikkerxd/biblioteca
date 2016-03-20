# -*- encoding: utf-8 -*-

from django import forms
from apps.lector.models import Lector


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
            mensaje = 'el lector no esta registrado'
            raise forms.ValidationError(mensaje)
        return cleaned_data
