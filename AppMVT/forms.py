from django import forms


class AutoFormulario(forms.Form):
    fabricante=forms.CharField(max_length=20)
    nombre=forms.CharField(max_length=20)
    motor=forms.IntegerField()
    modelo=forms.IntegerField()

class MotoFormulario(forms.Form):   
    fabricante=forms.CharField(max_length=20)
    nombre=forms.CharField(max_length=20)
    motor=forms.IntegerField()
    modelo=forms.IntegerField()

class CamionetaFormulario(forms.Form):   
    fabricante=forms.CharField(max_length=20)
    nombre=forms.CharField(max_length=20)
    motor=forms.IntegerField()
    modelo=forms.IntegerField()

class MotorBusqueda(forms.Form):
    motor=forms.IntegerField()