from rest_framework import serializers
from admision_api.core.models.resultado import Resultado

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'
