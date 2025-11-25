from rest_framework import viewsets
from admision_api.core.models.estudiante import Estudiante
from admision_api.core.serializers.estudiante import EstudianteSerializer
from admision_api.core.permissions import IsAdminOrReadOnly

class EstudianteViewSet(viewsets.ModelViewSet):

    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAdminOrReadOnly]
