from django.conf.urls import patterns, include, url


urlpatterns = patterns('payment.modules.paypal.views',
    url(r'^standard/$', 'paypal_standard', name='payment_paypal_standard'),
)
