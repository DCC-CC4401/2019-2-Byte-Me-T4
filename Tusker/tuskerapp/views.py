from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import SignUpForm, SignInForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import sys


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def user_profile(request):
    user = request.user
    avatar = UserProfile.objects.get(user=user).picture
    return render(request, 'userProfile.html',
                  context={"user_name":user.first_name,
                           "user_last_name": user.last_name,
                           "user_email": user.email,
                           "avatar": avatar})


def landing_page(request):
    user = request.user
    if request.user.is_authenticated:
        avatar = UserProfile.objects.get(user=user).picture
        return render(request, 'landingPage.html', context={"user_name": user.first_name,
                                                        "avatar": avatar})
    else:
        messages.error(request, "Something is wrong with your credentials")
        return render(request, 'index.html')


def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            form = SignInForm(request.POST, request.FILES)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=email, password=raw_password)
                if user is None:
                    messages.error(request, 'email or password not correct')
                else:
                    login(request, user)
                    messages.success(request, f'Inicio de Sesión Exitoso para {email}!')
                    return redirect('/landingPage/')

        elif request.POST.get('submit') == 'sign_up':
            form = SignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data['password']

                user.set_password(password)
                user.save()
                image = UserProfile(user=user, picture=request.FILES['picture'])
                image.save()
                messages.success(request, f'Cuenta creada con éxito! {user}')
                return redirect('/index/')
            else:
                messages.error(request, form.errors)
    return render(request, 'index.html', context={"up_form": SignUpForm(), "in_form": SignInForm(),
                                                  "image_form": UserProfileForm()})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            user = request.user.username
            password = form.cleaned_data['new_password1']
            user = authenticate(username=user, password=password)
            if user is None:
                messages.error(request, form.errors)
                return redirect('/index/')
            else:
                login(user,password)
                return redirect('/landingPage/')
    return render(request, 'changePassword.html',
                  context={"password_form": PasswordChangeForm(user=request.user)})


def update_user(request):
    user_profile2 = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        print("its a POST request :)", file=sys.stderr)
        update_profile_form = UserProfileForm(data=request.POST, instance=user_profile2)
        if update_profile_form.is_valid():
            profile = update_profile_form.save()
            profile.user = request.user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return redirect('/profile/')
        else:
            print(update_profile_form.errors, file=sys.stderr)
    else:
        update_profile_form = UserProfileForm(instance=user_profile2)
    return render(request, 'changeProfilePicture.html', {'update_profile_form': update_profile_form})
