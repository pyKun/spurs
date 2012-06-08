from django.conf.urls.defaults import *

urlpatterns = patterns('apps.test.views',
    (r'^$', 'home'),
)
