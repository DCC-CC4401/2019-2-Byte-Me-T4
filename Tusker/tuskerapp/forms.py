from django.contrib.auth.models import User
from django import forms


class SignInForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
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
