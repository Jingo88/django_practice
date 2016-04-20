from django.conf.urls import url, include

from .views import(
	
	)

from todos import views

urlpatterns = [
	url(r'^all', views.all_),
	url(r'^incomplete', views.incomplete),
	url(r'^date', views.date),
	url(r'^save', views.save_),
	url(r'^complete', views.complete),
	url(r'^update', views.update),
	url(r'^delete', views.delete),
]