"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(route = "",view = views.MyView.as_view(),name = "index"),
    path(route = "login/",view = views.LoginView.as_view(),name = "login"),
    path(route = "logout/",view = views.log_out,name = "logout"),
    path(route = "signup/",view = views.register,name = "signup")
]
