"""
URL configuration for whatsapp project.

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
from django.urls import path, include
from whatsapp.views import upper_case, login, about, base, sample

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calls/', include('calls.urls')),
    path(route='upper/<name>/', view=upper_case, name="upper"),
    path(route='login/', view=login, name="login"),
    path(route='about/<x>/<y>/', view=about, name="about"),
    path(route='base/<data>/', view=base, name="base"),
    path(route='sample/', view=sample, name="sample"),



]
