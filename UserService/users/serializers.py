from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    # Hyperlinked to use url and not pk to represent relationship
    class Meta:
        model = CustomUser
        fields = ('username', 'exp', 'level')