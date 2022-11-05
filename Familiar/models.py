from django.db import models

# Create your models here.
class Familiar (models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    fecha_nac = models.DateField(null=True)
    parentezco = models.CharField(max_length=40, null=True)