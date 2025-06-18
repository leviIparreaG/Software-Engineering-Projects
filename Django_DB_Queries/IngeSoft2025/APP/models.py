from django.db import models

# Create your models here.
class Grupo (models.Model):
    id_grupo = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Grupo {self.id_grupo}"

class Estudiante (models.Model):
    numCta = models. IntegerField (default=0)
    nombres = models. CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    # Aqui guardamos los grupos de un alumno
    grupos = models.ManyToManyField (Grupo, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"