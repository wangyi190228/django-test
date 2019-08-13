from django.db import models

# Create your models here.
class Attendinfo(models.Model):
    staffnum = models.PositiveIntegerField()
    attdate = models.DateField()
    weekday = models.CharField(max_length = 20)

    starttime = models.CharField(max_length = 10)
    verifyS = models.CharField(max_length = 30)
    stoptime = models.CharField(max_length = 10)
    verifyT = models.CharField(max_length = 30)

    machine = models.CharField(max_length = 10)
    hours = models.FloatField()

    # def __str__(self):
    #     return self.staffnum


    
    
