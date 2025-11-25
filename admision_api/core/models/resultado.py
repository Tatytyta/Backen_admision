from django.db import models
from admision_api.core.models.solicitud import Solicitud

class Resultado(models.Model):
    solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE)
    fecha_resultado = models.DateField()
    resultado = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=200)
