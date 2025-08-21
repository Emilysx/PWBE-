from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor, Editora, Livro
from .serializers import AutoSerializers, EditoraSerializers, LivroSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class AutoresView(ListCreateAPIView): # ListCreateAPIView é o post
    queryset = Autor.objects.all() 
    serializer_class = AutoSerializers
    # set é enviar e o get é para pegar


@api_view(['GET', 'POST'])
def visu_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutoSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers

class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers


