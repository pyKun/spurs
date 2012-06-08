from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'home.views.home'),
    (r'^test/', include('apps.test.urls')),
)
