from django.conf.urls import patterns, url

from category import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<cate_name>\D+)/$', views.chart, name='chart'),
)