from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissions

from .serializers import ChallengeSerializer
from .models import Challenge

@permission_classes([DjangoModelPermissions]) 
class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all().order_by('doneTime')
    serializer_class = ChallengeSerializer
    