from django.db import models

class Activity(models.Model):
	name = models.CharField(max_length=)
	category = models.IntegerField()
	desc = models.CharField(max_length=)
	user_id = models.IntegerField()
	datetime = models.DateTimeField()
	duration = models.TimeField()

class ActivityTemplate(models.Model):
	name = models.CharField(max_length=)
	category = models.IntegerField()
	desc = models.CharField(max_length=)
	user_id = models.IntegerField()

class Relations(models.Model):
	user_id1 = models.IntegerField()
	user_id2 = models.IntegerField()
	status = models.IntegerField()
