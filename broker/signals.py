from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)


def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)

def badges(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='badges')
        instance.groups.add(group)
        Badges.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(badges, sender=User)


def pin(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='pin')
        instance.groups.add(group)
        Pin.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(pin, sender=User)

def kyc(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='kyc')
        instance.groups.add(group)
        Kyc.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(kyc, sender=User)