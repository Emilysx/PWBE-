from rest_framework import serializers # a serializers tranforma a tabela em json
from .models import Autor, Editora, Livro

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        #Caso se eu quiser colocar campos definidos a sintaxe seria assim:
        # ['id', 'nome', '...']

class EditoraSerializers(serializers.ModelSerializer): # pode ser um padrão ou não...
    class Meta:
        model = Editora
        fields = '__all__'

        
class LivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
