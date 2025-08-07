from rest_framework import serializers # a serializers tranforma a tabela em json
from .models import Autor

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        

