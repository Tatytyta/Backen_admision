from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admision_api.core.models.solicitud import Solicitud
from admision_api.core.serializers.solicitud import SolicitudSerializer

class SolicitudViewSet(viewsets.ModelViewSet):

    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [IsAuthenticated]
