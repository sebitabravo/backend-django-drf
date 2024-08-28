# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import programmerSerializer
from .models import programmer

# Create your views here.


class programmerViewSet(viewsets.ModelViewSet):
    # Creacion de una consulta o QUERY a nuestra tabla, trayendo todos los campos como objeto.
    queryset = programmer.objects.all()
    # Agregamos la clase programmerSerializer que ya tiene el modelo serializado para mostrar.
    serializer_class = programmerSerializer
