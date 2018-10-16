"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from core import views

urlpatterns = [
    path('core/login/', auth_views.LoginView.as_view(template_name='core/registration/login.html'), name='core-login'),
    path('core/logout/', auth_views.LogoutView.as_view(next_page='/'), name='core-logout'),
    path('core/sign-up/', views.core_sign_up, name='core-sign-up'),
    path('core/', views.core_home, name='core-home'),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)