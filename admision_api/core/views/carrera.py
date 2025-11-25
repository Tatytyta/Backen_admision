from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admision_api.core.models.carrera import Carrera
from admision_api.core.serializers.carrera import CarreraSerializer

class CarreraViewSet(viewsets.ModelViewSet):

    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
    permission_classes = [IsAuthenticated]
