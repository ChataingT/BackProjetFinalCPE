from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    exp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
