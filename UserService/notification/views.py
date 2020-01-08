from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissions

from .serializers import NotificationSerializer
from .models import Notification

@permission_classes([DjangoModelPermissions]) 
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('sendTime')
    serializer_class = NotificationSerializer
    