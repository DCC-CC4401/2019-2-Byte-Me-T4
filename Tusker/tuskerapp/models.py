from django.contrib.auth.models import User
from django.db import models

from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()
    desc = models.TextField()
    user_id = models.ForeignKey(User, models.CASCADE)
    datetime = models.DateTimeField()
    duration = models.TimeField()


class ActivityTemplate(models.Model):
    name = models.TextField()
    category = models.IntegerField()
    desc = models.TextField()
    user_id = models.IntegerField()


class Relations(models.Model):
    user_id1 = models.IntegerField()
    user_id2 = models.IntegerField()
    status = models.IntegerField()