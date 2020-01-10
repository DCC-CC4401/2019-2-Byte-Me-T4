from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.core.files.images import get_image_dimensions


class SignInForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('email', 'password')


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    username = forms.EmailField(max_length=150, label="Email")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def save(self, commit=True):
        user = super().save(False)
        user.email = user.username
        user = super().save()
        return user


class UserProfileForm(forms.ModelForm):
    picture = forms.FileField(required=True, label="Imagen de Perfil")
    class Meta:
        model = UserProfile
        fields = ('picture',)
