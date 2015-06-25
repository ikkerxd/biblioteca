# -*- encoding: utf-8 -*-
from django import forms

from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        label='usuario',
        max_length='30',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )
    password = forms.CharField(
        label='contraseña',
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('usuario o contraseña incorrecta ..!!')
        return self.cleaned_data
