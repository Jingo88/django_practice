from django import forms
from django.contrib.auth.models import User
from .models import Leader
from django.core.validators import RegexValidator

class UserSignUp(forms.ModelForm):
	
	# Validator Jeff Made in case you want to add it
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$',
		'This value may contain only letters, '
		'numbers and _ characters.')

	# Had to set up this empty string so that bullshit default helptext doesn't appear. Thanks Django
	username = forms.CharField(widget=forms.TextInput(
		),
		help_text="",
		required = True,
		min_length = 6,
	)
	password = forms.CharField(widget=forms.PasswordInput(),
		required = True,
		min_length = 6,
		validators=[alphanumeric]
	)

	class Meta:
		model = User
		fields = [
			"username",
			"password",
		]

class LeaderSignUp(forms.ModelForm):

	class Meta:
		model = Leader
		fields = [
			"first_name",
			"last_name",
			"bio",
		]
