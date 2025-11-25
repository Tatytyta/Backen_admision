from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admision_api.core.models.instituto import Instituto
from admision_api.core.serializers.instituto import InstitutoSerializer

class InstitutoViewSet(viewsets.ModelViewSet):

    queryset = Instituto.objects.all()
    serializer_class = InstitutoSerializer
    permission_classes = [IsAuthenticated]
