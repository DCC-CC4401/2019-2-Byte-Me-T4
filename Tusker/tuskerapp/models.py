from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Activity(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(CustomUser, models.CASCADE)
    datetime = models.DateTimeField()
    duration = models.TimeField()

class ActivityTemplate(models.Model):
    name = models.TextField()
    category = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(CustomUser, models.CASCADE)

class Relations(models.Model):
    user_1 = models.ForeignKey(CustomUser, models.CASCADE, related_name="user1")
    user_2 = models.ForeignKey(CustomUser, models.CASCADE, related_name="user2")
    status = models.IntegerField()
