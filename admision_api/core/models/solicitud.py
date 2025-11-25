from django.db import models
from admision_api.core.models.estudiante import Estudiante
from admision_api.core.models.carrera import Carrera

class Solicitud(models.Model):
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
