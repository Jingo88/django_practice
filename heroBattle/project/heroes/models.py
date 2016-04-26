from django.db import models
from django.contrib.auth.models import User

# added default blank for bio. "Blank will appear in the text field on the sign up page"
class Leader(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	bio = models.TextField(max_length=500, default='blank')

