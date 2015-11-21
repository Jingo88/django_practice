from django.conf.urls import url

from . import views

# Manual multiple views
#######
# urlpatterns = [
# 	# This will go to /polls/
# 	url(r'^$', views.index,name='index'),
# 	# This will go to /polls/(number 0-9)/
# 	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# 	# This will go to /polls/(number 0-9)/results
# 	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
# 	# This will go to /polls/(number 0-9)/vote
# 	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]


# Django's Generic Views

urlpatters = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
