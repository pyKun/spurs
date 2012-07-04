from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('apps.test.views',
    (r'^google/$', 'google'),
    (r'^dbg/$', 'dbg'),
    (r'^dbg2/$', 'dbg2'),
    (r'^search/$', 'search'),
    (r'^update/$', 'update'),
    (r'^$', 'test'),
    (r'^account_test/$', 'account_test_page'),
)

urlpatterns += staticfiles_urlpatterns()
