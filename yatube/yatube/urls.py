"""yatube URL Configuration

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
from django.contrib import admin
<<<<<<< HEAD
from posts import views 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
=======
from django.urls import path

from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
>>>>>>> be3674557d6818f3f9386a83a7f90ff13d410aaa
]
