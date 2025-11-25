from django.db import models
from admision_api.core.models.instituto import Instituto

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_anios = models.IntegerField()
    instituto = models.ForeignKey(Instituto, on_delete=models.CASCADE)
