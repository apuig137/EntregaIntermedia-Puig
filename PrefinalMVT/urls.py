"""PrefinalMVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from AppMVT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name="inicio"),
    path('autos/', views.autos,name="autos"),
    path('motos/', views.motos,name="motos"),
    path('camionetas/', views.camionetas,name="camionetas"),
    #path('autoFormulario/', views.autoFormulario, name="autoFormulario"),
    path('autoBusqueda/', views.autoBusqueda, name="autoBusqueda"),
    path('autoBusqueda/PrefinalMVT/mostrarAuto/', views.mostrarAuto, name="mostrarAuto"),
    path('motoBusqueda/', views.motoBusqueda, name="motoBusqueda"),
    path('motoBusqueda/PrefinalMVT/mostrarMoto/', views.mostrarMoto, name="mostrarMoto"),
    path('camionetaBusqueda/', views.camionetaBusqueda, name="camionetaBusqueda"),
    path('camionetaBusqueda/PrefinalMVT/mostrarCamioneta/', views.mostrarCamioneta, name="mostrarCamioneta"),
]
