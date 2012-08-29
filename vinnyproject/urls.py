from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'root.html'}, name='root'),
    url(r'^home/$', direct_to_template, {'template': 'homepage.html'}, name='home'),
    url(r'^land/$', direct_to_template, {'template': 'landing.html'}, name='land'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    url(r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)

# Should remove if static files served separately (e.g. S3, etc.)
from django.conf import settings
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
)   
