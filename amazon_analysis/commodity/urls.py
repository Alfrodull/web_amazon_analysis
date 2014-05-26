from django.conf.urls import patterns, url

from commodity import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'p', views.search, name='search'),
	# url(r'^(?P<asin>\w\w+)/$', views.chart, name='chart'),
)