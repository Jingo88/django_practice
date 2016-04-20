from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from .validators import *


# def min_validation(value):
# 	if len(value) < 5:
# 		raise ValidationError("{} is invalid, must have more than 5 characters". format(value))
# Create your models here.

class Post(models.Model):
	brand = models.CharField(max_length = 50, validators=[min_validation])
	brand_type = models.CharField(max_length = 80, validators=[min_validation])
	description = models.TextField(validators=[min_validation])
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	brand_email = models.EmailField(max_length = 50, blank=True)

	def __str__(self):
		return self.brand
		# return "{} {}".format(self.brand, self.brand_type)

	def get_absolute_url(self):
		
		return reverse("posts:detail", kwargs={"id":self.id})