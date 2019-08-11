from django.db import models

# Create your models here.
class attendinfo(models.Model):
    staffnum = models.PositiveIntegerField()
    attdate = models.DateField()
    weeknum = models.CharField(max_length = 20)
    starttime5 = models.CharField(max_length = 10)
    stoptime5 = models.CharField(max_length = 10)
    starttime4 = models.CharField(max_length = 10)
    stoptime4 = models.CharField(max_length = 10)
    starttime3 = models.CharField(max_length = 10)
    stoptime3 = models.CharField(max_length = 10)
    hours = models.PositiveSmallIntegerField()
    machine = models.CharField(max_length = 10)
    verify = models.CharField(max_length = 30)
