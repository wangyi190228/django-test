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

class Alapply(models.Model):
    staffnum = models.PositiveIntegerField()
    alstartdate = models.DateField()
    starttime = models.CharField(max_length = 10)
    alstopdate = models.DateField()
    stoptime = models.CharField(max_length = 10)
    aldays = models.PositiveSmallIntegerField()

class Alinfo(models.Model):
    staffnum = models.PositiveIntegerField()
    applicant = models.CharField(max_length = 32)
    aplitime = models.DateTimeField()
    reason = models.TextField()
    leader = models.CharField(max_length = 32)
    fapltime = models.DateTimeField()
    fapl = models.BooleanField()
    freason = models.TextField()
    hr = models.CharField(max_length = 32)
    sapl = models.BooleanField()
    sreason = models.TextField()






