"""Tusker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from Tusker import settings
from tuskerapp import views as app_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', app_views.user_profile, name="profile"),
    path('landingPage/', app_views.landing_page, name="landingPage.html"),
    path('index/', app_views.index, name="index.html"),
    path('logout', app_views.logout_view, name='logout.html'),
    path('changePassword/', app_views.change_password, name='changePassword.html'),
    path('changeProfilePicture/', app_views.update_user, name='changeProfilePicture.html'),
]

# urlpatterns += staticfiles_urlpatterns()




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
