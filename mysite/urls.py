from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import hello, current_time, hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_time),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
