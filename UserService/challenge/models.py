from django.db import models
from users.models import CustomUser

class Challenge(models.Model):
    """
    A sportive challenge
    """
    userPk = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now_add=True) #save the create date time
    doneTime = models.DateTimeField() #when the challenged has been done
    custom = models.BooleanField() # if it was a custom one
    duration = models.DurationField() # time duration of the effort
    difficulty = models.IntegerField() # difficulty level 
    length = models.FloatField() # in KM, length or the run
    effortType = models.IntegerField() #type of effort: constant run, fract...
    completion = models.FloatField() # percentage of completion

    
    def __str__(self):
        return str((self.notifId, self.sendTime))
