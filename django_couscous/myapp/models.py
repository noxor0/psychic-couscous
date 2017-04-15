from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    skill = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)# * Decimal(10)
    lat = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    lng = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'User'

class UserHike(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    trailid = models.CharField(db_column='trailID', max_length=50)  # Field name made lowercase.
    liked = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'User_Hike'
        unique_together = (('userid', 'trailid'),)

class Trail(models.Model):
    trailid = models.CharField(db_column='trailID', primary_key=True, max_length=255)  # Field name made lowercase.
    trailname = models.CharField(db_column='trailName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficulty = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    lat = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    lng = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Trail'
