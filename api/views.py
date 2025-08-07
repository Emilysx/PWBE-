from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor
from .serializers import AutoSerializers

class AutoresView(ListCreateAPIView): # ListCreateAPIView é o post
    queryset = Autor.objects.all()
    serializer_class = AutoSerializers
    # set é enviar e o get é para pegar
