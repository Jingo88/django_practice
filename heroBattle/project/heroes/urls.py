from django.conf.urls import url
from django.contrib import admin

from .views import (
	Leader_Login,
	IndexView
)

urlpatterns=[
	url(r'^login/$', Leader_Login.as_view(), name="login"),
	url(r'^$', IndexView.as_view(), name="index")
]