from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib import messages


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def user_profile(request):
    return render(request, 'userProfile.html',
                  context={"user_name":request.user.first_name,
                           "user_last_name": request.user.last_name,
                           "user_email": request.user.email})


def landing_page(request):
    return render(request, 'landingPage.html', context={"user_name": request.user.first_name})


def index(request):
    if request.method == "POST":

        # Sign In #
        if request.POST.get('submit') == 'sign_in':
            form = SignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                #print("email " + email + "pass " + raw_password)
                user = authenticate(username=email, password=raw_password)
                #print(user)
                if user is None:
                    messages.error(request, 'email or password not correct')
                else:
                    login(request, user)
                    messages.success(request, f'Inicio de Sesión Exitoso para {email}!')
                    #print(user.first_name)
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
    return render(request, 'index.html', context={"up_form": SignUpForm(), "in_form": SignInForm()})


