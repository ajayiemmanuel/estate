from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from .forms import UserRegistrationForm, UserLoginForm, SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
from typing import Protocol
from django.core.mail import send_mail
from django.conf import settings




def index(request):
    context = {}
    return render (request, "broker/index.html", context)

def about(request):
    context = {}
    return render (request, "broker/about.html", context)

@login_required (login_url = "login")
def add_fund(request):
    user = request.user

    addfunds = user.addfund_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        transaction = request.POST.get('transaction')
        gateway = request.POST.get('gateway')
        amount = request.POST.get('amount')
        charge = request.POST.get('charge')
        status = request.POST.get('status')
        time = request.POST.get('time')


        addfund, created = Addfund.objects.get_or_create(
            user=user,
            name=name,
            transaction=transaction,
            gateway=gateway,
            amount=amount,
            charge=charge,
            status=status,
            time=time
            )

        return redirect('add_fund_confirm')

    context = {'addfunds': addfunds}
    return render (request, "broker/add_fund.html", context)

@login_required (login_url = "login")
def add_fund_confirm(request):
    user = request.user

    addfunds = Addfund.objects.filter(user=user)
    context = {'addfunds': addfunds}
    return render (request, "broker/add_fund_confirm.html", context)

@login_required (login_url = "login")
def badges(request):
    context = {}
    return render (request, "broker/badges.html", context)

def contact(request):

   if request.method == 'POST':
       name = request.POST.get('name')
       message = request.POST.get('message')
       email = request.POST.get('email')
       ctx = {
           'name' : name,
           'message' : message,
           'email' : email
       }
       message = render_to_string('broker/referral_bonus.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['ajayiohiremen046@gmail.com'], 
        fail_silently=False, html_message=message)
   return render(request, 'broker/contact.html')

@login_required (login_url = "login")
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render (request, "broker/change_password.html", {'form': form})

@login_required (login_url = "login")
def dashboard(request):

    return render (request, "broker/dashboard.html")

def faqs(request):
    context = {}
    return render (request, "broker/faqs.html", context)

@login_required (login_url = "login")
def fund_history(request):
    user = request.user

    addfunds = Addfund.objects.filter(user=user)
    context = {'addfunds': addfunds}
    return render (request, "broker/fund_history.html", context)

def get_started(request):
    context = {}
    return render (request, "broker/get_started.html", context)

@login_required (login_url = "login")
def add_fund_confirm1(request):
    context = {}
    return render (request, "broker/add_fund_confirm1.html", context)

@login_required (login_url = "login")
def invest_history(request):
    user = request.user

    investments = Investment.objects.filter(user=user)
    context = {'investments': investments}
    return render (request, "broker/invest_history.html", context)

@login_required (login_url = "login")
def investment_properties(request):
    user = request.user

    categories = Property.objects.filter(user=user)
    context = {'categories': categories}
    return render (request, "broker/investment_properties.html", context)

@login_required (login_url = "login")
def investprime_support_ticket(request):
    context = {}
    return render (request, "broker/investprime_support_ticket.html", context)

@login_required (login_url = "login")
def money_transfer(request):
    user = request.user

    withdraws = user.withdraw_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        transaction = request.POST.get('transaction')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        remark = request.POST.get('remark')
        status = request.POST.get('status')
        time = request.POST.get('time')


        withdraw, created = Withdraw.objects.get_or_create(
            user=user,
            name=name,
            transaction=transaction,
            email=email,
            amount=amount,
            remark=remark,
            status=status,
            time=time
            )
            
        return redirect('pin')

    context = {'withdraws': withdraws}
    return render (request, "broker/money_transfer.html", context)

@login_required (login_url = "login")
def my_investment_properties(request):
    return render (request, "broker/my_investment_properties.html")

@login_required (login_url = "login")
def my_offered_properties(request):
    context = {}
    return render (request, "broker/my_offered_properties.html", context)

@login_required (login_url = "login")
def my_shared_properties(request):
    context = {}
    return render (request, "broker/my_shared_properties.html", context)

@login_required (login_url = "login")
def payout_history(request):
    user = request.user

    wiretransfers = Wiretransfer.objects.filter(user=user)
    banktransfers = Banktransfer.objects.filter(user=user)
    bitcoins = Bitcoin.objects.filter(user=user)

    context = {'wiretransfers':wiretransfers, 'banktransfers':banktransfers, 'bitcoins':bitcoins}
    return render (request, "broker/payout_history.html", context)

@login_required (login_url = "login")
def payout1(request):
    user = request.user

    wiretransfers = user.wiretransfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        transaction = request.POST.get('transaction')
        bank = request.POST.get('bank')
        accountnumber = request.POST.get('accountnumber')
        gateway = request.POST.get('gateway')
        swift = request.POST.get('swift')
        amount = request.POST.get('amount')
        charge = request.POST.get('charge')
        status = request.POST.get('status')
        time = request.POST.get('time')


        wiretransfer, created = Wiretransfer.objects.get_or_create(
            user=user,
            name=name,
            bank=bank,
            transaction=transaction,
            accountnumber=accountnumber,
            gateway=gateway,
            swift=swift,
            amount=amount,
            charge=charge,
            status=status,
            time=time
            )
       
        return redirect('pin')

    context = {'wiretransfers': wiretransfers}
    return render (request, "broker/payout1.html",context)

@login_required (login_url = "login")
def payout2(request):
    user = request.user

    banktransfers = user.banktransfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        transaction = request.POST.get('transaction')
        bank = request.POST.get('bank')
        accountnumber = request.POST.get('accountnumber')
        gateway = request.POST.get('gateway')
        swift = request.POST.get('swift')
        amount = request.POST.get('amount')
        charge = request.POST.get('charge')
        status = request.POST.get('status')
        time = request.POST.get('time')


        banktransfer, created = Banktransfer.objects.get_or_create(
            user=user,
            name=name,
            bank=bank,
            transaction=transaction,
            accountnumber=accountnumber,
            gateway=gateway,
            swift=swift,
            amount=amount,
            charge=charge,
            status=status,
            time=time
            )

        return redirect('pin')

    context = {'banktransfers': banktransfers}    
    return render (request, "broker/payout2.html", context)


@login_required (login_url = "login")
def payout3(request):
    user = request.user

    bitcoins = user.bitcoin_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        transaction = request.POST.get('transaction')
        wallet = request.POST.get('wallet')
        gateway = request.POST.get('gateway')
        amount = request.POST.get('amount')
        charge = request.POST.get('charge')
        status = request.POST.get('status')
        time = request.POST.get('time')


        bitcoin, created = Bitcoin.objects.get_or_create(
            user=user,
            name=name,
            transaction=transaction,
            wallet=wallet,
            gateway=gateway,
            amount=amount,
            charge=charge,
            status=status,
            time=time
            )
        
        return redirect('pin')

    context = {'bitcoins':bitcoins}    
    return render (request, "broker/payout3.html", context)

@login_required (login_url = "login")
def payout(request):
    context = {}
    return render (request, "broker/payout.html", context)


def pricing(request):
    context = {}
    return render (request, "broker/pricing.html", context)

@login_required (login_url = "login")
def profile(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/profile.html", context)

@login_required (login_url = "login")
def create(request):

   if request.method == 'POST':
       name = request.POST.get('name')
       message = request.POST.get('message')
       subject = request.POST.get('subject')
       ctx = {
           'name' : name,
           'message' : message,
           'subject' : subject
       }
       message = render_to_string('broker/add_fund_confirm1.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['ajayiohiremen046@gmail.com'], 
        fail_silently=False, html_message=message)
   return render(request, 'broker/create.html')

@login_required (login_url = "login")
def property_share_market(request):
    context = {}
    return render (request, "broker/property_share_market.html", context)

@login_required (login_url = "login")
def receive_offered_properties(request):
    context = {}
    return render (request, "broker/receive_offered_properties.html", context)

@login_required (login_url = "login")
def referral_bonus(request):
    context = {}
    return render (request, "broker/referral_bonus.html", context)

@login_required (login_url = "login")
def referral(request):
    context = {}
    return render (request, "broker/referral.html", context)

@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="broker/register.html",
        context={"form": form}
        )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("dashboard")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="broker/login.html",
        context={"form": form}
        )



@login_required (login_url = "login")
def password_reset( request):
    return render (request, 'broker/password_reset.html') 


@user_not_authenticated
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("broker/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('login')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="broker/password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'broker/change_password.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("login")



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')



def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("broker/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def template_activate_account(request):
    context = {}
    return render (request, "broker/template-activate-account.html", context)


def reset(request):
    context = {}
    return render (request, "broker/reset.html", context)

def service(request):
    context = {}
    return render (request, "broker/service.html", context)


@login_required (login_url = "login")
def transaction(request):
    user = request.user

    withdraws = Withdraw.objects.filter(user=user)
    context = {'withdraws': withdraws}
    return render (request, "broker/transaction.html", context)

@login_required (login_url = "login")
def wish_list_property(request):
    context = {}
    return render (request, "broker/wish_list_property.html", context)

def learn_more(request):
    context = {}
    return render (request, "broker/learn_more.html", context)

def crypto_fx(request):
    user = request.user

    categories = user.property_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        property_name = request.POST.get('property_name')
        property_address = request.POST.get('property_address')
        first_amount = request.POST.get('first_amount')
        second_amount = request.POST.get('second_amount')
        description = request.POST.get('description')
        expire = request.POST.get('expire')
        image = request.FILES.getlist('image')
        image1 = request.FILES.getlist('image1')
        image2 = request.FILES.getlist('image2')
        image3 = request.FILES.getlist('image3')
        image4 = request.FILES.getlist('image4')
        image5 = request.FILES.getlist('image5')
        image6 = request.FILES.getlist('image6')

        if data['property'] != 'none':
            property = Property.objects.get(id=data['property'])
        elif data['property_new'] != '':
            property, created = Property.objects.get_or_create(
                user=user,
                name=data['property_new'],
                property_name=property_name,
                property_address=property_address,
                first_amount=first_amount,
                second_amount=second_amount,
                description=data['description'],
                image=image,
                image1=image1,
                image2=image2,
                image3=image3,
                image4=image4,
                image5=image5,
                image6=image6,
                expire=expire
                )

        return redirect('make_investement')

    context = {'categories': categories}
    return render (request, "broker/crypto_fx.html", context)

@login_required(login_url='login')
def viewPhoto(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'broker/photo.html', {'property': property})

@login_required (login_url = "login")
def make_investement(request):
    user = request.user

    investments = user.investment_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        amount = request.POST.get('amount')
        profit = request.POST.get('profit')
        up_coming = request.POST.get('up_coming')
        action = request.POST.get('action')
        running_invest = request.POST.get('running_invest')


        investment, created = Investment.objects.get_or_create(
            user=user,
            name=name,
            amount=amount,
            profit=profit,
            up_coming=up_coming,
            action=action,
            running_invest=running_invest
            )

        return redirect('dashboard')

    context = {'investments': investments}    
    return render (request, "broker/make_investement.html", context)

@login_required (login_url = "login")
def pin(request):
    return render (request, "broker/pin.html")


@login_required (login_url = "login")
def pay_successfully( request):
    return render (request, 'broker/pay-successfully.html') 

@login_required (login_url = "login")
def Identity_verification( request):
    kyc = request.user.kyc
    form = KycForm (instance = kyc)

    if request.method == 'POST':
        form = KycForm (request.POST, request.FILES, instance = kyc)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, 'broker/Identity_verification.html', context) 