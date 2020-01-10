from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField


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


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

