from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', 'apps.home.views.home'),
    (r'^test/', include('apps.test.urls')),
)

urlpatterns += staticfiles_urlpatterns()
