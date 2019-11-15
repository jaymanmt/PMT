from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from .models import MyUser, ReferralCode
from django.contrib.auth.decorators import login_required
from PMT.views import home
from django.utils.crypto import get_random_string
from django.utils import timezone

# Create your views here.

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('home'))

def login(request):
    #user clicked on submit
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        #input validation, followed by:
        #authenticate to see if the username and pw matches anything in the database. 
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            #if there is a user and pw that matches
            
            if user:
                messages.success(request, "You have successfully logged in")
                auth.login(user=user, request=request)
                return redirect(reverse('shop'))
            else:
                messages.error(request, "We couldn't find a match, please try again.")
                return redirect(reverse('login'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {
            "form":form
        })

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password2'])
            if user:
                unique_id = get_random_string(length=10)
                code = ReferralCode()
                code.discount = unique_id
                code.active = True
                code.save()
                auth.login(user=user, request=request)
                user.referral_code = code
                user.save()
                messages.success(request,"You have registered successfully")
            else:
                messages.error(request, "Your registration has failed")
            return redirect(reverse('home'))
        else:
            return render(request, 'accounts/register.template.html', {
                'form':form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.template.html',{
            'form':form
        })
def partner(request):
    return render(request, 'accounts/partner.html')
    
def user_profile(request):
    #search by email in object as each email is unique to each user
    user = MyUser.objects.filter(email=request.user.email).first()
    return render(request, 'accounts/profile.html', {
        "profile":user
    })
    
def edit_profile(request):
    if request.method == "POST":
        pass

#to add a POST in order to do CRU_ on the user's profile
