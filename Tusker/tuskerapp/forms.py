from django import forms

class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

