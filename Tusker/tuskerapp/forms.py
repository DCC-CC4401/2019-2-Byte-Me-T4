from django.contrib.auth.models import User
from tuskerapp.models import UserProfile
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
    profile_picture = forms.FileField()
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

    def clean_avatar(self):
        avatar = self.cleaned_data['profile_picture']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar