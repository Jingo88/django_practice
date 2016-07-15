from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Post
from django.views.generic import View



# Time to make class based views.

class Posts_List(View):
	def get(self, request):
		all_posts = Post.objects.all()
		context = {
			"all_posts": all_posts,
		}
		return render(request, "posts/list.html", context)




def blah(self, request):

	blah = Post.objects.all()

	return redirect(posts:list)


# # Create your views here.
# def index(request):
# 	if request.GET.get("post"):
# 		context = {
# 			"post": request.GET.get("post")
# 		}
# 	else:
# 		context = {
# 			"post": "No Post Yet!!!!"
# 		}
# 	return render(request, 'index.html', context)

# def posts(request):

# 	if request.method == "POST":
# 		post = request.POST["post-data"]
# 		print(post)
# 		return redirect("/?post={}".format(post))
# 	if request.method == "GET":
# 		return render(request, 'posts.html', {})

# def create(request):
# 	return render(request, 'create.html', {})
