from django.conf.urls import patterns, url

from create import views

urlpatterns = patterns('',
	# http://127.0.0.1:8000/create/ 
	url(r'^new$', views.create_page, name='create-new'),
	# http://127.0.0.1:8000/create/?firstname=bardia&lastname=heydari&email=az.Bardia13%40gmail.com&password=123123&year=1994&month=12&day=9&avatar=1379437_556748381063252_1266131993_n.jpg&tel=09123456789&country=iran&city=tehran&sex=male&submit=Create
	url(r'', views.create , name='create-done'),
)
