from django.db import models

class Auto(models.Model):
    fabricante=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    motor=models.IntegerField()
    modelo=models.IntegerField()

class Moto(models.Model):
    fabricante=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    motor=models.IntegerField()
    modelo=models.IntegerField()

class Camioneta(models.Model):
    fabricante=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    motor=models.IntegerField()
    modelo=models.IntegerField()