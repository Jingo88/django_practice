from django.conf.urls import url
from django.contrib import admin

from .views import (
	Leader_Login,
	index_view,
	logout_view,
	SignUp_View
)

urlpatterns=[
	url(r'^login/$', Leader_Login.as_view(), name="login"),
	url(r'^logout/$', logout_view, name="logout"),
	url(r'^signup/$', SignUp_View.as_view(), name="signup"),
	url(r'^$', index_view, name="index")
]