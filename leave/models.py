from django.db import models

# Create your models here.
class staffAl(models.Model):
    staffnum = models.PositiveIntegerField()
    startdate = models.DateField()
    stopdate = models.DateField()
    expirydate = models.DateField()
    Alsum = models.PositiveSmallIntegerField()
    remain = models.PositiveSmallIntegerField()
    used = models.PositiveSmallIntegerField()

class Alinfo(models.Model):
    starttime = models.CharField(max_length = 50)
    stoptime = models.CharField(max_length = 50)
    aldays = models.PositiveSmallIntegerField()
    applicant = models.CharField(max_length = 32)
    aplitime = models.DateTimeField()
    reason = models.TextField()
    leader = models.CharField(max_length = 32)
    fapltime = models.DateTimeField()
    freason = models.TextField()
    hr = models.CharField(max_length = 32)
    sreason = models.TextField()
    # submitted canceled processed finished
    status = models.CharField(max_length = 20)






