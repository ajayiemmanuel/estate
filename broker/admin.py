from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register (Customer)
admin.site.register(Withdraw)
admin.site.register(Addfund)
admin.site.register(Wiretransfer)
admin.site.register(Banktransfer)
admin.site.register(Bitcoin)
admin.site.register(Deposit)
admin.site.register(Property)
admin.site.register(Investment)
admin.site.register(Badges)
admin.site.register (Pin)
admin.site.register (Kyc)