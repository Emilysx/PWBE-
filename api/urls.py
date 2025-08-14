from django.urls import path
from .views import AutoresView, visu_autor

urlpatterns = [ 
    path('autores', AutoresView.as_view()),
    path('autores/lista',visu_autor )
]
# é uma lista que define como as URLs. ela diz ao Django qual função de visualização (view) deve ser executada 
# quando um usuário acessa uma determinada URL. 
