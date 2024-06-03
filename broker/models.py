from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models




# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    first_name = models.CharField (max_length = 200,  null = True)
    last_name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    address = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)
    bio = models.TextField (max_length = 200, null = True)

    def __str__(self):
        return str(self.name)

class Withdraw(models.Model):
    class Meta:
        verbose_name = 'Withdraw'
        verbose_name_plural = 'Withdraws'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200, null=False, blank=False)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True)
    remark = models.TextField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Addfund(models.Model):
    class Meta:
        verbose_name = 'Addfund'
        verbose_name_plural = 'Addfunds'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.TextField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Wiretransfer(models.Model):
    class Meta:
        verbose_name = 'Wiretransfer'
        verbose_name_plural = 'Wiretransfers'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    bank = models.CharField(max_length=254, null=True, blank=True)
    accountnumber = models.CharField(max_length=254, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    swift = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Banktransfer(models.Model):
    class Meta:
        verbose_name = 'Banktransfer'
        verbose_name_plural = 'Banktransfers'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    bank = models.CharField(max_length=254, null=True, blank=True)
    accountnumber = models.CharField(max_length=254, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    swift = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Bitcoin(models.Model):
    class Meta:
        verbose_name = 'Bitcoin'
        verbose_name_plural = 'Bitcoins'
        
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    transaction = models.CharField(max_length=250, null=True, blank=True)
    wallet = models.CharField(max_length=250, null=True, blank=True)
    gateway = models.CharField(max_length=254, null=True, blank=True)
    amount = models.CharField(max_length=250, null=True, blank=True, default = "$10")
    charge = models.CharField(max_length=250, null=True, blank=True, default = "pending")
    status = models.CharField(max_length=250, null=True, blank=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    main_balance = models.CharField (max_length = 200,  null = True, default = "30")
    intrest_balance = models.CharField (max_length = 200,  null = True, default = "0")
    total_deposit = models.CharField (max_length = 200, null = True, default = "0")
    total_payout = models.CharField (max_length = 200, null = True, default = "0")
    total_invest = models.CharField (max_length = 200, null = True, default = "0")

    def __str__(self):
        return str(self.name)

class Property(models.Model):
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    property_name = models.CharField(max_length=100, null=False, blank=False)
    property_address = models.CharField(max_length=100, null=False, blank=False)
    first_amount = models.CharField(max_length=100, null=False, blank=False)
    second_amount = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    image1 = models.ImageField(null=False, blank=False)
    image2 = models.ImageField(null=False, blank=False)
    image3 = models.ImageField(null=False, blank=False)
    image4 = models.ImageField(null=False, blank=False)
    image5 = models.ImageField(null=False, blank=False)
    image6 = models.ImageField(null=False, blank=False)


    def __str__(self):
        return str(self.name)

class Investment (models.Model):
    class Meta:
        verbose_name = 'Investment'
        verbose_name_plural = 'Investments'
        
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    amount = models.CharField (max_length = 200,  null = True)
    profit = models.CharField (max_length = 200,  null = True)
    up_coming = models.CharField (max_length = 200,  null = True)
    action = models.CharField (max_length = 200, null = True)
    running_invest = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return str(self.name)

badge1 = (
    ('locked', 'locked'),
    ('open', 'open'),
    )

badge2 = (
    ('locked', 'locked'),
    ('open', 'open'),
    )

badge3 = (
    ('locked', 'locked'),
    ('open', 'open'),
    )

badge4 = (
    ('locked', 'locked'),
    ('open', 'open'),
    )


bonus = (
    ('0', 'Level0'),
    ('1000', 'Level1'),
    ('2000', 'Level2'),
    ('5000', 'Level3'),
    ('5000', 'Level4'),
    )

level = (
    ('X', 'X'),
    ('1', '1'),
    ('2', '2'),
    ('3', '4'),
    ('4', '4'),
    )

class Badges (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    badge1 = models.CharField (max_length=24, choices=badge1, default='locked')
    badge2 = models.CharField (max_length=24, choices=badge2, default='locked')
    badge3 = models.CharField (max_length=24, choices=badge3, default='locked')
    badge4 = models.CharField (max_length=24, choices=badge4, default='locked')
    bonus = models.CharField (max_length=24, choices=bonus, default='0')
    level = models.CharField (max_length=24, choices=level, default='X')

    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


class Kyc (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    valid_idcard_front = models.ImageField (null = True, blank = True)
    valid_idcard_back = models.ImageField (null = True, blank = True)


    def __str__(self):
        return str(self.name)