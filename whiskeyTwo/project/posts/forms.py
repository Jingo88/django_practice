from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = [
			"brand",
			"brand_type",
			"description",
			"price",
			"brand_email"
		]