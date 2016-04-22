from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Leader(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

# class Hero(models.Models):
# 	blah = models.ManytoMany()
