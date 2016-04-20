from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Post
from posts.forms import PostForm
from django.views.generic import View
from django.core.exceptions import ValidationError

###########################################################################
##############		WE ARE CREATING CLASS BASED VIEWS 	###################
###########################################################################

class Posts_List(View):
	def get(self, req):
		whiskey_list = Post.objects.all()
		context = {
			"whiskey_list": whiskey_list,
		}
		return render(req, "posts/list.html", context)

class Posts_Detail(View):
	detail_template = 'posts/detail.html'

	def get(self, req, **kwargs):
		whiskey = get_object_or_404(Post, id=kwargs['id'])
		context = {
			"whiskey":whiskey
		}
		return render(req, self.detail_template, context)

# You can also use this to store your context
	# def get_context_data(self, **kwargs):

class Posts_Create(View):
	form_class = PostForm
	initial = {'key': 'value'}
	create_template = 'posts/create.html'

	def get(self, req, *args, **kwargs):
		create_form = self.form_class(initial=self.initial)
		context = {
			"create": create_form
		}
		return render(req, self.create_template, context)

	def post(self, req, *args, **kwargs):
		create_form = self.form_class(req.POST or None)
		# try:
		# 	if create_form.brand_email: 
		# 		print('da fuq is going on?')
		# except:
		# 	EmailValidator(
		# 	message="That is not a valid Email", 
		# 	code = None,
		# 	whitelist = None,)
		if create_form.is_valid():
			instance = create_form.save(commit=False)
			instance.save()
			return redirect(instance)
		context = {
			"create":create_form,
		}
		return render(req, self.create_template, context)

class Posts_Update(View):
	form_class = PostForm
	# initial = {'key': 'value'}
	update_template = 'posts/update.html'

	def get(self, req, *args, **kwargs):
		whiskey = get_object_or_404(Post, id=kwargs['id'])
		update_form = self.form_class(req.POST or None, instance = whiskey)
		context = {
			"whiskey": update_form
		}
		return render(req, self.update_template, context)

	def post(self, req, *args, **kwargs):
		whiskey = get_object_or_404(Post, id=kwargs['id'])
		update_form = self.form_class(req.POST or None, instance = whiskey)
		if update_form.is_valid():
			instance = update_form.save(commit=False)
			instance.save()
			return redirect(instance)
		context = {
			"whiskey":update_form,
		}
		return render(req, self.update_template, context)

class Posts_Delete(View):

	def get(self, req, **kwargs):
		instance = get_object_or_404(Post, id=kwargs['id'])		
		instance.delete()
		# have to set permanent to True
		return redirect('posts:list', permanent=True)






###########################################################################
############		WE ARE CREATING FUNCTION BASED VIEWS	###############
###########################################################################

# def posts_list(req):
# 	whiskey_list = Post.objects.all()
# 	context = {
# 		"whiskey_list" : whiskey_list,
# 	}
# 	return render(req, "posts/list.html", context)

# def posts_create(req):
# 	create_form = PostForm(req.POST or None)

# 	if create_form.is_valid():
# 		instance = create_form.save(commit=False)
# 		instance.save()
# 		# return HttpReponseRedirect(instance.get_absolute_url())
# 		return redirect(instance)
# 	context = {
# 		"create":create_form,
# 	}
# 	return render(req, "posts/create.html", context)

# def posts_detail(req, id=None):
# 	whiskey = get_object_or_404(Post, id=id)
# 	print(whiskey.id)
# 	context = {
# 		"whiskey": whiskey
# 	}
# 	return render(req, "posts/detail.html", context)

# def posts_update(req, id=None):

# 	whiskey = get_object_or_404(Post, id=id)

# # "initial" is a attribute of a form set?
# 	# update_form = PostForm(initial = {
# 	# 	"brand": whiskey.brand, 
# 	# 	"brand_type": whiskey.brand_type,
# 	# 	"price" : whiskey.price,
# 	# 	"description": whiskey.description
# 	# 	})
# # instance = whiskey is something learned from Jeff
# 	update_form = PostForm(req.POST or None, instance = whiskey)
# 	print(update_form)
# 	if update_form.is_valid():
# 		instance = update_form.save()
# 		# instance.save()
# 		return redirect(instance)
# 	context = {
# 		"whiskey": update_form,
# 	}

# 	# PostForm(data=request.POST)
# 	return render(req, "posts/update.html", context)





