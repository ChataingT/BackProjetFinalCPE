from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    """
    Notification send to the user to motivate him to do a challenge
    """
    userPk = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notifId = models.IntegerField()
    sendTime = models.DateTimeField()
    displayed = models.BooleanField(default=False)
    
    def __str__(self):
        return str((self.notifId, self.sendTime))
