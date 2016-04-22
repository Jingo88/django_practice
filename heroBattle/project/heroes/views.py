from django.shortcuts import render, HttpResponse
from .models import Leader
from django.views.generic import View


# Create your views here.

class Leader_Login(View):

	def get(self, request):
		return render(request, 'heroes/login.html', {})

	def post(self, request):
		blah = request.POST
		print(blah.items())

		return HttpResponse("Hello World")