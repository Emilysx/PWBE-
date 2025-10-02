from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Editora, Livro
from .serializers import AutoSerializers, EditoraSerializers, LivroSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated # Permissões
from django_filters.rest_framework import DjangoFilterBackend # Filtros
from rest_framework.filters import SearchFilter # Filtros

from .filters import AutoFilter


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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


###################### AUTORES ###########################
class AutoresView(ListCreateAPIView): # ListCreateAPIView é o post
    queryset = Autor.objects.all() 
    serializer_class = AutoSerializers
    # permission_classes = [IsAuthenticated]

    # set é enviar e o get é para pegar
    # Filtro
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id']
    search_fields = ['nome', 'sobrenome']
    # filtro
    filterset_class = AutoFilter



class AutoresDetailView( RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all() 
    serializer_class = AutoSerializers
    # permission_classes = [IsAuthenticated]

###################### EDITORAS ###########################
class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers
    # permission_classes = [IsAuthenticated]

class EditorasDetailView( RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers
    # permission_classes = [IsAuthenticated]


###################### LIVROS ###########################
class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers
    # permission_classes = [IsAuthenticated]

class LivrosDetailView( RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers
    # permission_classes = [IsAuthenticated]



