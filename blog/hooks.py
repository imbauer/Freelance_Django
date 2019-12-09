from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(valid_ipn_received)
def show_me_the_money(sender, **kwargs):
    t = User.objects.get(username=sender.custom)


    if sender.item_name == "basic":
        initial = t.profile.tokens
        final = t.profile.tokens + 1
        t.profile.tokens = t.profile.tokens + 1  # change field
        t.profile.invoice_count = t.profile.invoice_count + 1

    elif sender.item_name == "standard":
        initial = t.profile.tokens
        final = t.profile.tokens + 2
        t.profile.tokens = t.profile.tokens + 2  # change field
        t.profile.invoice_count = t.profile.invoice_count + 1

    elif sender.item_name == "custom":
        initial = t.profile.tokens
        final = t.profile.tokens + sender.item_number
        t.profile.tokens = t.profile.tokens + sender.item_number  # change field
        t.profile.invoice_count = t.profile.invoice_count + 1

    else:
        initial = t.profile.tokens
        final = t.profile.tokens + 5
        t.profile.tokens = t.profile.tokens + 5  # change field
        t.profile.invoice_count = t.profile.invoice_count + 1

    t.save() # this will update only

    print("show_me_the_money: ")
    ipn_obj = sender
    print("show_me_the_money: " + ipn_obj.payment_status)

@receiver(invalid_ipn_received)
def do_not_show_me_the_money(sender, **kwargs):
    print("none: ")
    ipn_obj = sender
    print("none: " + ipn_obj.payment_status)
