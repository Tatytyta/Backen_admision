from rest_framework import serializers
from admision_api.core.models.carrera import Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
