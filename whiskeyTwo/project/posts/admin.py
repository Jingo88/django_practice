from django.contrib import admin
from posts.models import Post
# Register your models here.

# admin.site.register(Post)

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["brand", "brand_type", "price"]
	search_fields = ["brand", "price"]

	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)