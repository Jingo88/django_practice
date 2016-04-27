from django.db import models
from django.contrib.auth.models import User

# added default blank for bio. "Blank will appear in the text field on the sign up page"
class Leader(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	bio = models.TextField(max_length=500, default='blank')
	hero_name = models.CharField(max_length=40, default = "blank")
	age = models.PositiveSmallIntegerField(default = 0)

	def __str__(self):
		return self.user.username
	

class Power(models.Model):
	name = models.CharField(max_length=40)
	method = models.CharField(max_length=40)
	description = models.TextField(max_length=500, default='blank')
	leader = models.ManyToManyField(Leader)

	def __str__(self):
		return self.name
