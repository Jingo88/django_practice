from django.shortcuts import render, redirect, HttpResponse
from .models import Leader, Power
from django.contrib.auth.models import User
from django.views.generic import View
from django import forms
from django.contrib.auth import authenticate, login, logout
from .forms import LeaderSignUp, UserSignUp
from django.contrib.auth.hashers import make_password


def index_view(request):
	# user == "AnonymousUser" unless they already logged in. Then it will be the username
	user = request.user
	print(user)

	if user.is_authenticated():

		# grab the User object and use it to grab the Leader object
		profile = User.objects.get(username=user)
		leader = Leader.objects.get(user = profile)
		power = Power.objects.all()
		context = {
			"profile" : profile,
			"leader": leader,
			"power": power
		}		
		return render(request, 'heroes/leader.html', context)
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

			# target the user instance from the form submit
			user_instance = user_submit_form.save(commit=False)

			# hash the password being generated
			user_instance.password = make_password(user_submit_form.cleaned_data['password'])

			# save the user. Must do this before we can attach the leader
			user_instance.save()

			# create the leader instance and save it
			leader_instance = Leader(
				user=user_instance, 
				first_name = leader_first_name,
				last_name = leader_last_name,
				bio = leader_bio
				)

			# save leader
			leader_instance.save()

			# if all this saves properly we redirect to the home page so they could log in
			return redirect('heroes:index')

		else: 
			# need to fix what happens when they enter bad information
			return HttpResponse("The information you entered was not valid")

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

		# authenticates returns True or None
		user = authenticate(username=username, password=password)

		print(user)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('heroes:index')

		# decide on what you want to do if the log in fails
		elif user == None:
			return HttpResponse("The Authentication method did not pass")



