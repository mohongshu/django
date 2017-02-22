from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import hello, current_time, hours_ahead
from books.views import display_meta
from books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
)
