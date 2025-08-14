from rest_framework import serializers # a serializers tranforma a tabela em json
from .models import Autor

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        #Caso se eu quiser colocar campos definidos a sintaxe seria assim:
        # ['id', 'nome', '...']
        

