from rest_framework import serializers
from .models import Persona

class ProyectoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = ('id', 'nombre', 'apellido', 'descripcion', 'fecha_add')
    read_only_fields = ('created_at',)