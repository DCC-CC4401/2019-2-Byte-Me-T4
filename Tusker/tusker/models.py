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

#class User(models.Model):
#	user_id = models.IntegerField()
#	name = models.CharField(max_length=)
#	last_name = models.CharField(max_length=)
#	emil = models.CharField(max_length=)
#	photo_address = models.CharField(max_length=)
#	emil = models.CharField(max_length=)
	


#class FarmAnimal(models.Model):
#        animal_name = models.CharField(max_length = 15)
#        nbr_legs = models.IntegerField(default=4)
#
#        def __str__(self):
#                return self.animal_name
