from django.conf.urls import url
from django.contrib import admin

###########################################################################
##########	URL Patters Class Based Views		###############
###########################################################################
from .views import(
	Posts_List,
	Posts_Create,
	Posts_Detail,
	Posts_Update,
	Posts_Delete,
	)

urlpatterns = [
	url(r'^$', Posts_List.as_view(), name='list'),
	url(r'^create$', Posts_Create.as_view(), name='create'),
	url(r'^(?P<id>\d+)/$', Posts_Detail.as_view(), name='detail'),
	url(r'^(?P<id>\d+)/update$', Posts_Update.as_view(), name='update'),
	url(r'^(?P<id>\d+)/delete$', Posts_Delete.as_view(), name='delete'),	
]


###########################################################################
##########	URL Patterns Function Based Views		###############
###########################################################################

# from .views import(
# 	posts_list,
# 	posts_create,
# 	posts_detail,
# 	posts_update,
# 	)

# urlpatterns = [
# 	url(r'^$', posts_list, name='list'),
# 	url(r'^create$', posts_create, name='create'),
# 	url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
# 	url(r'^(?P<id>\d+)/update$', posts_update, name='update'),
# ]