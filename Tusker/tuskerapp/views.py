from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from tuskerapp.models import UserProfile
from .forms import SignUpForm, SignInForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def user_profile(request):
    user = request.user
    avatar = UserProfile.objects.get(user=user).profile_picture
    return render(request, 'userProfile.html',
                  context={"user_name":user.first_name,
                           "user_last_name": user.last_name,
                           "user_email": user.email,
                           "avatar": avatar})


def landing_page(request):
    user = request.user
    if request.user.is_authenticated:
        avatar = UserProfile.objects.get(user=user).profile_picture
        return render(request, 'landingPage.html', context={"user_name": user.first_name,
                                                        "avatar": avatar})
    else:
        messages.error(request, "Something is wrong with your credentials")
        return render(request, 'index.html')

def index(request):
    if request.method == "POST":

        # Sign In #
        if request.POST.get('submit') == 'sign_in':
            form = SignInForm(request.POST, request.FILES)
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
            form = SignUpForm(request.POST, request.FILES)
            #print("recibe Sign Up", form.errors)
            #print("FILES", request.FILES)
            if form.is_valid():
                print("From is Valid")
                user = form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data['password']
                #  Use set_password here
                user.set_password(password)
                user.save()
                image = UserProfile(user=user, profile_picture=request.FILES['profile_picture'])
                image.save()
                #print("email " + str(email) + "pass " + str(password))
                #print(login(request, user))
                messages.success(request, f'Cuenta creada con éxito! {user}')
                return redirect('http://127.0.0.1:8000/index/')
            else:
                messages.error(request, form.errors)
    return render(request, 'index.html', context={"up_form": SignUpForm(), "in_form": SignInForm(),
                                                  "image_form": UserProfileForm()})


def change_password(request):
    # Validation
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            username = request.user.username
            password = form.cleaned_data['new_password1']
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, form.errors)
                return redirect('http://127.0.0.1:8000/index/')
            else:
                login(request, user)
                return redirect('http://127.0.0.1:8000/landingPage/')
    # Show Form
    return render(request, 'changePassword.html',
                  context={"password_form": PasswordChangeForm(user=request.user)})

# def change_profile(request):
#     user = request.user
#     avatar = UserProfile.objects.get(user=user).profile_picture
#     current_password = user.password
#
#     # Validation
#     if request.method == "POST":
#         form = EditUserForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_password = form.cleaned_data['password']
#             # If passwords are equal prompt an error
#         else:
#             messages.error(request, form.errors)
#     # Show Form
#     return render(request, 'editUser.html', context={"edit_form": EditUserForm(),
#                                                      "image_form": EditUserProfileForm(),
#                                                      "user_name": user.first_name,
#                                                      "user_last_name": user.last_name,
#                                                      "user_email": user.email,
#                                                      "avatar": avatar, })
