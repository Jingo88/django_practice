from django.shortcuts import render, redirect, HttpResponse
from .models import Leader
from django.contrib.auth.models import User
from django.views.generic import View
from django import forms
from django.contrib.auth import authenticate, login, logout
from .forms import LeaderSignUp, UserSignUp
from django.contrib.auth.hashers import make_password

# Create your views here.

def index_view(request):
	# user == "AnonymousUser" unless they already logged in. Then it will be the username
	user = request.user
	print(user)

	if user.is_authenticated():
		print(request.session.items())
		return render(request, 'heroes/leader.html', {})
	else:
		return render(request, 'base.html', {})

def logout_view(request):
	logout(request)
	return redirect('heroes:index')

class SignUp_View(View):
	# made two model forms for the sign up page. One for the Django User and the other for our Leader model
	user_form = UserSignUp
	leader_form = LeaderSignUp
	initial = {'key': 'value'}

	# GET request that will pass the forms to the signup html
	def get(self, request, *args, **kwargs):
		l_signup_form = self.leader_form(initial=self.initial)
		u_signup_form = self.user_form(initial=self.initial)
		context = {
			"leader": l_signup_form,
			"user" : u_signup_form
		}
		return render(request, 'heroes/signup.html', context)

	def post(self,request,*args, **kwargs):
		# Take the form information
		user_submit_form = self.user_form(request.POST or None)
		leader_submit_form = self.leader_form(request.POST or None)
		
		# check if both are valid
		if user_submit_form.is_valid() and leader_submit_form.is_valid():
			
			# cleaned data allows us to target a tag from the form through it's "name" and it will return the value
			leader_first_name = leader_submit_form.cleaned_data['first_name']
			leader_last_name = leader_submit_form.cleaned_data['last_name']
			leader_bio = leader_submit_form.cleaned_data['bio']

			username = user_submit_form.cleaned_data['username']
			password = user_submit_form.cleaned_data['password']

			user_instance = user_submit_form.save(commit=False)
			user_instance.password = make_password(user_submit_form.cleaned_data['password'])
			user_instance.save()



			# user_instance = User(username=username, password=password)
			# We have to save the user instance before we save the leader because the leader user attribute 
			# user_instance = user_submit_form.save(commit=False)

			print(user_submit_form)
			print(user_instance.password)

			# user_instance.save()

			x = User.objects.get(username=user_instance.username)
			print(x)

			# create the leader instance and save it
			leader_instance = Leader(
				user=user_instance, 
				first_name = leader_first_name,
				last_name = leader_last_name,
				bio = leader_bio
				)

			leader_instance.save()
			# if all this saves properly we redirect to the home page
			return redirect('heroes:index')


class Leader_Login(View):

# Do not need to pass in "*args, **kwargs" into the method parameters
# Not using model forms for Django User Model b/c it's fucking dumb

	def get(self, request):
		return render(request, 'heroes/login.html', {})

# Django auth comes with the authenticate and login methods
	def post(self, request):
		# username = request.POST.get('username')
		# password = request.POST.get('password')
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)

		user = authenticate(username=username, password=password)

		print(user)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('heroes:index')
		else:
			return HttpResponse("You're not allowed here")



