from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.http import JsonResponse
import requests

# Create your views here.

class Index_View(View):
	template = 'movies/index.html'

	def get(self, request):
		return render(request, self.template, {})

class Search_All(View):
	url = 'http://www.omdbapi.com/?s='
	# use requests params to dynamic url

	def get(self, request):
		title = request.GET["title"]

		search_title = title.replace(" ", "+")
		
		url_end = self.url + search_title

		# control flow status_code check
		omdb_req = requests.get(url_end).json()


		print(omdb_req)
		content = {
			"movie": url_end
		}
		return JsonResponse(omdb_req)





	# def post(self, request, title):
	# 	print(request)
	# 	search_title = title.replace(" ", "+")
	# 	url_end = self.url + search_title

	# 	content = {
	# 		"movie": url_end
	# 	}
	# 	return JsonResponse(content)








