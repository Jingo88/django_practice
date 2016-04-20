from django.db import models

# Create your models here.


class User(models.Model):
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 25)
	age = models.IntegerField()
	bio = models.TextField()


	def __str__(self):
		return self.username
		# return "{} {}".format(self.brand, self.brand_type)

	# def get_absolute_url(self):
	# 	print()
	# 	return reverse("posts:detail", kwargs={"id":self.id})