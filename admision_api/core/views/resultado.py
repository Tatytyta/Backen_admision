from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from admision_api.core.models.resultado import Resultado
from admision_api.core.serializers.resultado import ResultadoSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    permission_classes = [IsAuthenticated]
