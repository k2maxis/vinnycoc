from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from payment.modules.paypal import config


def paypal_standard(request):
    ipn_url = 'http://%s%s' % (Site.objects.get_current().domain, reverse("paypal-ipn"))
    pdt_url = 'http://%s%s' % (Site.objects.get_current().domain, reverse("paypal-pdt"))
    return_url = pdt_url if config.PDT else ipn_url

    data = {
        "amount": "1.00",
        "item_name": "Samsung Galaxy S3",
        "invoice": "INVOICE001",
        "notify_url": ipn_url,
        "return_url": return_url,
    }

    form = PayPalPaymentsForm(initial=data)
    data['form'] = form.sandbox() if config.DEBUG else form.render()

    return render_to_response("payment/paypal/standard.html", data,
           context_instance=RequestContext(request))
