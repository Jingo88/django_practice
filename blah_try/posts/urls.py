from django.conf.urls import url, include
from .views import Posts_List

urlpatterns = [
	# url(r'^create$', views.create, name='create'),
	url(r'^$', Posts_List.as_view(), name='list'),
]

