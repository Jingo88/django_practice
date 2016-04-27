from django.conf.urls import url
from django.contrib import admin
from .views import (
	Index_View,
	Search_All,
	)

urlpatterns = [
    url(r'^search', Search_All.as_view(), name='search'),
    url(r'^$', Index_View.as_view(), name='index'),
]