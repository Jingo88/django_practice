from django.conf.urls import url
from django.contrib import admin

###########################################################################
##########	URL Patters Class Based Views		###############
###########################################################################
from .views import(
	Users_Profile,
	Users_Register,
	Users_Login,
	# Users_Update,
	# Users_Delete,
	)

urlpatterns = [
	url(r'^$', Users_Profile.as_view(), name='profile'),
	url(r'^register$', Users_Register.as_view(), name='register'),
	url(r'^login$', Users_Login.as_view(), name='login'),
	# url(r'^(?P<id>\d+)/$', Posts_Detail.as_view(), name='detail'),
	# url(r'^(?P<id>\d+)/update$', Posts_Update.as_view(), name='update'),
	# url(r'^(?P<id>\d+)/delete$', Posts_Delete.as_view(), name='delete'),	
]