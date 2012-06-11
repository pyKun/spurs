from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('apps.test.views',
    (r'^google/$', 'google'),
    (r'^dbg/$', 'dbg'),
    (r'^search/$', 'search'),
)

urlpatterns += staticfiles_urlpatterns()
