from django.db import models

# Create your models here.
class Staffinfo(models.Model):
    staffnum = models.PositiveIntegerField()
    mailbox = models.EmailField(max_length = 128)
    hiredate = models.DateField()
    staffphone = models.CharField(max_length=20)
    stafftitle = models.CharField(max_length=20)
    leader = models.CharField(max_length=32)