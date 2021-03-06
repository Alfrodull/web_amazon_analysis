from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'amazon_analysis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^category/', include('category.urls', namespace="category")),
    url(r'^commodity/', include('commodity.urls', namespace="commodity")),
    url(r'^admin/', include(admin.site.urls)),
)
