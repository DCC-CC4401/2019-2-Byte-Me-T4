from django import forms

class IniciarSesionForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)