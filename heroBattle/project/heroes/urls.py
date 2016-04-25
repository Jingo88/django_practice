from django.conf.urls import url
from django.contrib import admin

from .views import (
	Leader_Login,
	index,
	logout_view
)

urlpatterns=[
	url(r'^login/$', Leader_Login.as_view(), name="login"),
	url(r'^logout/$', logout_view, name="logout"),
	url(r'^$', index, name="index")
]