from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissions

from .serializers import ActivitySerializer
from .models import Activity

@permission_classes([DjangoModelPermissions]) 
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('activityType')
    serializer_class = ActivitySerializer
    