from paypal.standard.ipn.signals import payment_was_successful


def ipn_successful(sender, **kwargs):
    ipn_obj = sender
    # Extra actions based on ipn_obj.custom
    # print something
payment_was_successful.connect(ipn_successful)
