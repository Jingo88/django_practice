from django.core.exceptions import ValidationError

def min_validation(value):
	if len(value) < 5:
		raise ValidationError("{} is invalid, must have more than 5 characters". format(value))