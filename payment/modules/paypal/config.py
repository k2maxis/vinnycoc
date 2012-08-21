from django.conf import settings

PDT = getattr(settings, 'PAYPAL_PDT', True)
DEBUG = getattr(settings, 'PAYPAL_DEBUG', True)
