# -*- encoding: utf-8 -*-
from django import forms


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
