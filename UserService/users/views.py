from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import DjangoModelPermissions, AllowAny

from .serializers import CustomUserSerializer
from .models import CustomUser

from .forms import CustomUserCreationForm

@permission_classes([AllowAny,])
#@api_view(['GET', 'POST'])
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#TODO controle for change about pwd and other
@permission_classes([DjangoModelPermissions]) 
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('username')
    serializer_class = CustomUserSerializer
    