from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissions

from .serializers import PlanningSerializer
from .models import Planning

@permission_classes([DjangoModelPermissions]) 
class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all().order_by('sendTime')
    serializer_class = PlanningSerializer
    