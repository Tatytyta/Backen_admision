from rest_framework import serializers
from admision_api.core.models.estudiante import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
