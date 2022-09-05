from django.http.request import QueryDict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppMVT.forms import AutoFormulario, MotoFormulario,CamionetaFormulario, MotorBusqueda
from AppMVT.models import Auto, Camioneta, Moto

def inicio(request):
    return render(request,"index.html")

def auto(request):
    return render(request,"auto.html")

def moto(request):
    return render(request,"moto.html")

def camioneta(request):
    return render(request,"camioneta.html")

def autos(request):
    if request.method == 'POST':
        miFormulario = AutoFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
                informacion = miFormulario.cleaned_data
                auto1 = Auto (nombre=informacion.get('nombre'), motor=informacion.get('motor'), fabricante=informacion.get('fabricante'), modelo=informacion.get('modelo'))
                auto1.save()
                return redirect("autos") #Vuelvo al inicio o a donde quieran
    autos=Auto.objects.all()
    contexto={
        "form":AutoFormulario(),
        "autos":autos
    }
    return render(request, "auto.html", contexto)

def autoBusqueda(request):
    contexto={
        "form":MotorBusqueda(),
    }
    return render(request,"autoBusqueda.html",contexto)
      
def mostrarAuto(request):
    motor=request.GET.get('motor')
    autos=Auto.objects.filter(motor__icontains=motor)
    contexto={
        "autos":autos
    }
    return render(request,"mostrarAuto.html",contexto)

def motos(request):
    if request.method == 'POST':
        miFormulario = MotoFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
                informacion = miFormulario.cleaned_data
                moto1 = Moto (nombre=informacion.get('nombre'), motor=informacion.get('motor'), fabricante=informacion.get('fabricante'), modelo=informacion.get('modelo'))
                moto1.save()
                return redirect("motos") #Vuelvo al inicio o a donde quieran
    motos=Moto.objects.all()
    contexto={
        "form":MotoFormulario(),
        "motos":motos
    }
    return render(request, "moto.html", contexto)

def motoBusqueda(request):
    contexto={
        "form":MotorBusqueda(),
    }
    return render(request,"motoBusqueda.html",contexto)
      
def mostrarMoto(request):
    motor=request.GET.get('motor')
    motos=Moto.objects.filter(motor__icontains=motor)
    contexto={
        "motos":motos
    }
    return render(request,"mostrarMoto.html",contexto)

def camionetas(request):
    if request.method == 'POST':
        miFormulario = CamionetaFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
                informacion = miFormulario.cleaned_data
                camioneta1 = Camioneta (nombre=informacion.get('nombre'), motor=informacion.get('motor'), fabricante=informacion.get('fabricante'), modelo=informacion.get('modelo'))
                camioneta1.save()
                return redirect("camionetas") #Vuelvo al inicio o a donde quieran
    camionetas=Camioneta.objects.all()
    contexto={
        "form":CamionetaFormulario(),
        "camionetas":camionetas
    }
    return render(request, "camioneta.html", contexto)

def camionetaBusqueda(request):
    contexto={
        "form":MotorBusqueda(),
    }
    return render(request,"camionetaBusqueda.html",contexto)
      
def mostrarCamioneta(request):
    motor=request.GET.get('motor')
    camionetas=Camioneta.objects.filter(motor__icontains=motor)
    contexto={
        "camionetas":camionetas
    }
    return render(request,"mostrarCamioneta.html",contexto)