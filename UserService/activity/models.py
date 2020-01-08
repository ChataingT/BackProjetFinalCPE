from django.db import models
from users.models import CustomUser

class Activity(models.Model):
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activityType = models.IntegerField()
    startTime = models.DateTimeField()
