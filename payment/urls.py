from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'payment/index.html'}, name='payment_index'),
	url(r'^paypal/',  include('payment.modules.paypal.urls')),
)
