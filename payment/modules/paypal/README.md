NOTES
=====

Wrapper of [django-paypal](https://github.com/dcramer/django-paypal).

The document of `django-paypal` is quite messy.

The document of Paypal integration is quite messy also.

Override `pdt/pdt.html` to adapt the layout, so must put
`payment.paypal.pdt` before `paypal.*` in `INSTALLED_APPS`.

Extra variable `PAYPAL_PDT` to select `PAYPAL_RECEIVER_EMAIL`,
`PAYPAL_IDENTITY_TOKEN` and `return_url`
