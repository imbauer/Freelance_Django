from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver

@receiver(valid_ipn_received)
def show_me_the_money(sender, **kwargs):
    messages.success(request, f'SHOW MONEY')
    return HttpResponseRedirect('/pricing')

@receiver(invalid_ipn_received)
def do_not_show_me_the_money(sender, **kwargs):
    messages.success(request, f'DO NOT SHOW MONEY')
    return HttpResponseRedirect('/paypal-cancel')
