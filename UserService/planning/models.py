from django.db import models
from users.models import CustomUser

class Planning(models.Model):
    """
    An activity represent a physical effort done by the user. It can be running,
    cycling, walking...
    """
    userPk = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notifId = models.IntegerField()
    sendTime = models.DateTimeField()
    
    def __str__(self):
        return str((self.notifId, self.sendTime))
