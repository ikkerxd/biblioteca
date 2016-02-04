from django import forms

class LectorPrestamoForm(forms.Form):
    Lector = forms.CharField(
        label='codigo',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )
