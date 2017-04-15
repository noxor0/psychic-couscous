from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.IntegerField()
    userName = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=8, decimal_places=4)
    lng = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
        return self.userName
