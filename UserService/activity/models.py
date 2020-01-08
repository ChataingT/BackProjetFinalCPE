from django.db import models
from users.models import CustomUser

class Activity(models.Model):
    """
    An activity represent a physical effort done by the user. It can be running,
    cycling, walking...
    """
    userPk = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activityType = models.IntegerField()
    startTime = models.DateTimeField()
    duration = models.DurationField
    
    def __str__(self):
        return self.activityType
