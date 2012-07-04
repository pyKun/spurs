from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'apps.home.views.home'),
    (r'^test/', include('apps.test.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^token/$','apps.test.views.token'),
    (r'^login/$', 'apps.accounts.views.login_page'),
    (r'^do_login/$', 'apps.accounts.views.do_login'),
    (r'^do_logout/$', 'apps.accounts.views.do_logout'),
)

urlpatterns += staticfiles_urlpatterns()
