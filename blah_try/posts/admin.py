from django.contrib import admin
from .models import Post

# Register your models here.

# Adding the Post model to the admin panel
# Admin Login "jasonng" and "1234abcd"

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	search_fields = ["title"]

	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
