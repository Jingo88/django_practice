from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from django import forms
from .forms import UserForm
from django.contrib.auth import authenticate

# Create your views here.

class Users_Profile(View):
	profile_template = 'users/profile.html'

	def get(self, req):
		users = User.objects.all()
		context = {
			"users": users,
		}
		return render(req, self.profile_template, context)

class Users_Register(View):
	register_template = 'users/register.html'
	profile_view = "users:profile"
	form_class = UserForm
	# initial = {'key': 'value'}	

	def get(self, req, *args, **kwargs):
		# register_form = self.form_class(initial = self.initial)
		register_form = self.form_class()
		context = {
			"register": register_form
		}
		return render(req, self.register_template, context)

	def post(self, req, *args, **kwargs):
		register_form = self.form_class(req.POST or None)
		if register_form.is_valid():
			instance = register_form.save(commit=False)
			instance.save()
			return redirect(self.profile_view)
		context = {
			"register": register_form
		}
		return render(req, self.profile_view, context)

class Users_Login(View):
	form_class = UserForm
	login_template = "users/login.html"
	profile_view = "users:profile"
	initial = {
		'username': "",
		'password': "",
	}

	def get(self, req, *args, **kwargs):
		login_form = self.form_class(initial = self.initial)
		# login_form = self.form_class()
		context = {
			"user": login_form
		}
		return render(req, self.login_template, context)

	def post(self,req,*args,**kwargs):
		login_form = self.form_class(req.POST or None)
		print("WHAT THE FUCK IS GOING ON")
		# if login_form.is_valid():
		username = req.POST['username']
		password = req.POST['password']
		print(username)
		print(password)
		user = authenticate(username = username, password = password)
		print(user)
		if user:
			print("WE ARE IN THE USER OF POST NOW!!!!")
			if user.is_active:
				print(req.session)
				req.session['user_id']=user.id
				req.session.set_expiry(10)
				return redirect(self.profile_view, username=req.session['id'])

		return redirect(self.profile_view)





















