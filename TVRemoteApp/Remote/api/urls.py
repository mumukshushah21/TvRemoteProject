from .views import Channellist
from django.conf.urls import url
from django.contrib import admin

urlpatterns=[
		url(r'^Channel/$',Channellist.as_view(),name='blog_list'),
		#url(r'^(?P<title>[\w-]+)/$',BlogDetailList.as_view(),name='blod_detail'),
		#url(r'^(?P<title>[\w-]+)/edit/$',BlogUpdateList.as_view(),name='blod_detail'),
]