from django.db import models

# Create your models here.
class Persona(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  descripcion = models.TextField()
  fecha_add = models.DateTimeField(auto_now_add=True)
  