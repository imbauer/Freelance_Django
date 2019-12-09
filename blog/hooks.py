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
            print("Small")
        elif ipn_obj.custom == "standard_plan":
            price = "2.20"
            print("Medium")
        elif ipn_obj.custom == "custom_plan":
            price = "3.30"
            print("Large")

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'CAD':
            print("Final Works")
    else:
        print("Did not work")
        return

valid_ipn_received.connect(show_me_the_money)
