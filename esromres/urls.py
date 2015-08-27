from django.conf.urls import patterns, include, url
from django.contrib import admin
from romres.views import index_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esromres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index_view, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
