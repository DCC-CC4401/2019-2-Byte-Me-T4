from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


def user_profile(request):
    return render(request, 'userProfile.html')


def landing_page(request):
    return render(request, 'landingPage.html')


def index(request):
    if request.method == "POST":

        # Sign In #
        if request.POST.get('submit') == 'sign_in':
            form = SignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                print("email " + email + "pass " + raw_password)
                user = authenticate(username=email, password=raw_password)
                print(user)
                if user is None:
                    messages.error(request, 'email or password not correct')
                else:
                    login(request, user)
                    messages.success(request, f'Inicio de Sesión Exitoso para {email}!')
                    return redirect('http://127.0.0.1:8000/landingPage/')

        # Sign Up #
        elif request.POST.get('submit') == 'sign_up':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data['password']
                #  Use set_password here
                user.set_password(password)
                user.save()
                login(request, user)
                messages.success(request, f'Cuenta creada con éxito! {user}')
                return redirect('http://127.0.0.1:8000/index/')
    return render(request, 'index.html', context={"upform": SignUpForm(), "inform": SignInForm()})


