from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),
    url(r'^admin/$', direct_to_template, {'template': 'root.html'}, name='root'),
    url(r'^home/$', direct_to_template, {'template': 'homepage.html'}, name='home'),
    url(r'^$', direct_to_template, {'template': 'landing.html'}, name='landing'),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}, name='about'),
    url(r'^jobs/$', direct_to_template, {'template': 'jobs.html'}, name='jobs'),
    url(r'^investors/$', direct_to_template, {'template': 'investors.html'}, name='investors'),
    url(r'^terms/$', direct_to_template, {'template': 'terms.html'}, name='terms'),
    url(r'^app-store/$', direct_to_template, {'template': 'appstore.html'}, name='appstore'),
    url(r'^google-play/$', direct_to_template, {'template': 'googleplay.html'}, name='googleplay'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^social/', include('socialregistration.urls', namespace='socialregistration')),
    url(r'^payment/', include('payment.urls')),
    url(r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    url(r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
    url(r'^ajax/login/$', 'vinnyproject.views.ajax_login', name='ajax_login'),
    url(r'^ajax/fb-connect/$', 'vinnyproject.views.facebook_connect', name='ajax_fb_connect'),
)

# Should remove if static files served separately (e.g. S3, etc.)
from django.conf import settings
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
)   
