from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != "sb-o81vn645225@business.example.com":
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "basic_plan":
            price = "1.10"
        elif ipn_obj.custom == "standard_plan":
            price = "2.20"
        elif ipn_obj.custom == "custom_plan":
            price = "3.30"

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'CAD':
            t = User.objects.get(username=request.user)
            initial = t.profile.tokens
            final = t.profile.tokens + 1
            t.profile.tokens = t.profile.tokens + 1  # change field
            t.profile.invoice_count = t.profile.invoice_count + 1
            t.save() # this will update only
    else:
        return

valid_ipn_received.connect(show_me_the_money)
