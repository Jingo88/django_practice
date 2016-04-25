from django import forms
from .models import Leader

class LeaderSignUp(forms.ModelForm):
	class Meta:
		model = Leader
		fields = [
			"user.username",
			"user.password",
			"first_name",
			"last_name",
			"bio",
		]



# Not using a model for for user login because that shit renders some weird annoying template

# from django.contrib.auth.models import User

# class UserLogin(forms.ModelForm):

# 	class Meta:
# 		model = User
# 		fields = [
# 			"username",
# 			"password",
# 		]