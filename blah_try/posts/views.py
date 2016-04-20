from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	if request.GET.get("post"):
		context = {
			"post": request.GET.get("post")
		}
	else:
		context = {
			"post": "No Post Yet!!!!"
		}
	return render(request, 'index.html', context)

def posts(request):

	if request.method == "POST":
		post = request.POST["post-data"]
		print(post)
		return redirect("/?post={}".format(post))
	if request.method == "GET":
		return render(request, 'posts.html', {})

def create(request):
	return redirect('posts:index')
