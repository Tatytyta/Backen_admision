from rest_framework import serializers
from admision_api.core.models.instituto import Instituto

class InstitutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituto
        fields = '__all__'
