from django import forms
from .models import User

class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = [
			"username",
			"password",
			"first_name",
			"last_name",
			"age",
			"bio",
		]