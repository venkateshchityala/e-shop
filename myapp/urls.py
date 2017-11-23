from django.conf.urls import include, url
from . import views

urlpatterns =[
	url(r'^$',views.home,name = 'home'),
	url(r'^add/$',views.ad_add,name ='add_ad'),
	url(r'^login/$',views.uLogin, name = 'login'),
	url(r'^logout/$',views.uLogout,name = 'logout'),
	url(r'^(?P<ad_id>[0-9]+)$',views.ad, name = 'ad'),


	]