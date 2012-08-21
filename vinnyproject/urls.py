from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', direct_to_template, {'template': 'homepage.html'}, name='home'),
    url(r'^payment/', include('payment.urls')),
    url(r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    url(r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)
