from django.urls import path
from .views import *

urlpatterns = [ 
    # GET / POST
    path('autores', AutoresView.as_view()),
    path('autores/lista',visu_autor ),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),

    # UPDATE / DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditorasDetailView.as_view()),
    path('livro/<int:pk>', LivrosDetailView.as_view()),


]
# é uma lista que define como as URLs. ela diz ao Django qual função de visualização (view) deve ser executada 
# quando um usuário acessa uma determinada URL. 
