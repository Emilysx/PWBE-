from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [ 
    # GET / POST
    path('autores', AutoresView.as_view()),
    path('autores/lista',visualizacao_autor ),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),
    path('buscar/', AutoresView.as_view()),

    # UPDATE / DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditorasDetailView.as_view()),
    path('livro/<int:pk>', LivrosDetailView.as_view()),

    # Token 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
# é uma lista que define como as URLs. ela diz ao Django qual função de visualização (view) deve ser executada 
# quando um usuário acessa uma determinada URL. 
