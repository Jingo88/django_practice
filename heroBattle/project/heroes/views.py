from django.shortcuts import render, HttpResponse
from .models import Leader
from django.views.generic import View
from django import forms
from django.contrib.auth import authenticate, login

# Create your views here.

class IndexView(View):
	def get(self, request):
		return render(request, 'base.html', {})

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
			login(request, user)
			return HttpResponse("Hello World")
		else:
			return HttpResponse("You're not allowed here")



