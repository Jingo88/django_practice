from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length = 35, blank=True)
	last_name = models.CharField(max_length = 35, blank=True)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.user.username