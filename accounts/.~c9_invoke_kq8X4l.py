from django.shortcuts import render, HttpResponse, reverse, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, UserEditProfile
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
    
def user_profile(request, id):
        
    get_user = get_object_or_404(MyUser, pk=id)
    
    if request.method == "POST":
        if "update_first_name" in request.POST:
            update_first_name = request.POST["update_first_name"]
            if update_first_name == "":
                pass
            else:
                get_user.first_name = update_first_name
                get_user.save()
        elif "update_last_name" in request.POST:
            update_last_name = request.POST["update_last_name"]
            if update_last_name == "":
                pass
            else:
                get_user.last_name = update_last_name
                get_user.save()
        elif "update_mobile" in request.POST:
            update_mobile = request.POST["update_mobile"]
            get_user.mobile = update_mobile
            get_user.save()
        
        return render(request, 'accounts/profile.html')

    else:
            
        #search by email in object as each email is unique to each user
        user = MyUser.objects.filter(email=request.user.email).first()
        return render(request, 'accounts/profile.html', {
            "profile":user
        })
    

#to add a POST in order to do CRU_ on the user's profile
