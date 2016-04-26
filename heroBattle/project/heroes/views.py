from django.shortcuts import render, redirect, HttpResponse
from .models import Leader
from django.views.generic import View
from django import forms
from django.contrib.auth import authenticate, login, logout
from .forms import LeaderSignUp, UserSignUp

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
	user_form = UserSignUp
	leader_form = LeaderSignUp
	initial = {'key': 'value'}

	def get(self, request, *args, **kwargs):
		l_signup_form = self.leader_form(initial=self.initial)
		u_signup_form = self.user_form(initial=self.initial)
		context = {
			"leader": l_signup_form,
			"user" : u_signup_form
		}
		return render(request, 'heroes/signup.html', context)

	def post(self,request,*args, **kwargs):
		user_submit_form = self.user_form(request.POST or None)
		leader_submit_form = self.leader_form(request.POST or None)
		print("CHECK OUT THESE SWEET FORMS")
		print(user_submit_form.is_valid())
		print(leader_submit_form.is_valid())

		if user_submit_form.is_valid() and leader_submit_form.is_valid():
			print("ARE WE IN THE POST AND IF STATEMENT")
			user_instance = user_submit_form.save(commit=False)
			leader_instance = leader_submit_form.save(commit=False)
			print(user_instance)
			print(leader_instance)

			user_instance.save()
			leader_instance.save()
			

		return redirect('heroes:index')


class Leader_Login(View):

# Do not need to pass in "*args, **kwargs" into the method parameters
# Not using model forms for Django User Model b/c it's fucking dumb

	def get(self, request):
		return render(request, 'heroes/login.html', {})

# Django auth comes with the authenticate and login methods
	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)

		user = authenticate(username=username,
							password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('heroes:index')
			else:
				return HttpResponse("You're not allowed here")



