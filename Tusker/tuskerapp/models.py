from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)
    datetime = models.DateTimeField()
    duration = models.TimeField()


class ActivityTemplate(models.Model):
    name = models.TextField()
    category = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)


class Relations(models.Model):
    user_1 = models.ForeignKey(User, models.CASCADE, related_name="user1")
    user_2 = models.ForeignKey(User, models.CASCADE, related_name="user2")
    status = models.IntegerField()
