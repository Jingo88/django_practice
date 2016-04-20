from django.db import models
import users

# Create your models here.

class Todo(models.Model):
	user_id = models.ForeignKey('users.Profile', blank=True)
	title = models.CharField(max_length = 50, blank=True)
	content = models.TextField(blank=True)

	def __str__(self):
		return self.title