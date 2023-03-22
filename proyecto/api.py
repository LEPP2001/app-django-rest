from proyecto.models import Persona
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Persona.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProyectoSerializer