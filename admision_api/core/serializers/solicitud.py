from rest_framework import serializers
from admision_api.core.models.solicitud import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
