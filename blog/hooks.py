from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(valid_ipn_received)
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
        t = User.objects.get(username="vanya7")
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "basic_plan":
            price = "1.10"
            print("Small")
            initial = t.profile.tokens
            final = t.profile.tokens + 1
            t.profile.tokens = t.profile.tokens + 1  # change field
            t.profile.invoice_count = t.profile.invoice_count + 1

        elif ipn_obj.custom == "standard_plan":
            price = "2.20"
            print("Medium")
            initial = t.profile.tokens
            final = t.profile.tokens + 2
            t.profile.tokens = t.profile.tokens + 2  # change field
            t.profile.invoice_count = t.profile.invoice_count + 2

        elif ipn_obj.custom == "custom_plan":
            price = "3.30"
            print("Large")
            initial = t.profile.tokens
            final = t.profile.tokens + 3
            t.profile.tokens = t.profile.tokens + 3  # change field
            t.profile.invoice_count = t.profile.invoice_count + 3

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'CAD':
            print("Final Works")
    else:
        print("Did not work")
        return





    t.save() # this will update only

    print("show_me_the_money: ")
    ipn_obj = sender
    print("show_me_the_money: " + ipn_obj.payment_status)

@receiver(invalid_ipn_received)
def do_not_show_me_the_money(sender, **kwargs):
    print("none: ")
    ipn_obj = sender
    print("none: " + ipn_obj.payment_status)
