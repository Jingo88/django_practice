from django.shortcuts import render, redirect, HttpResponse
from .models import Leader
from django.views.generic import View
from django import forms
from django.contrib.auth import authenticate, login, logout
from .forms import LeaderSignUp

# Create your views here.

def index_view(request):
	# user == "AnonymousUser" unless they already logged in. Then it will be the username
	user = request.user
	print(user)

	if user.is_authenticated():
		return render(request, 'heroes/leader.html', {})
	else:
		return render(request, 'base.html', {})

def logout_view(request):
	logout(request)
	return redirect('heroes:index')

class SignUp_View(View):
	form = LeaderSignUp
	initial = {'key': 'value'}

	def get(self, request, *args, **kwargs):
		signup_form = self.form(initial=self.initial)
		context = {
			"signup":signup_form
		}
		return render(request, 'heroes.signup.html', context)


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



