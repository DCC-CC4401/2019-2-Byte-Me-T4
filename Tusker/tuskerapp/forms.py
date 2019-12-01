from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class SignInForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password')
