from django.shortcuts import render, HttpResponse, reverse, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, UserEditProfile
from .models import MyUser, ReferralCode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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
        form = UserRegistrationForm(request.POST, request.FILES)
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
                user.photo = "images/user-icon.png"
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

def edit_profile(request, id):
    #search by email in object as each email is unique to each user
    get_user = MyUser.objects.filter(email=request.user.email, id=id).first()

    if request.method == "POST":
        
        edit_profile_form = UserEditProfile({
            "photo" : request.POST.get("photo"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "mobile": request.POST.get("mobile"),
            "email": request.POST.get("email"),
            "username": request.POST.get("username"),
            "injuries": request.POST.get("injuries"),
            "self_depict": request.POST.get("self_depict")
        })
        if 'photo' in request.FILES:
            try:
                edit_profile_form.fields["photo"].validate(request.FILES.get('photo'))
                get_user.photo = request.FILES.get('photo')
                get_user.save()
                messages.success(request, "Profile Photo Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        if 'first_name' in request.POST:
            try:
                edit_profile_form.fields["first_name"].validate(request.POST.get('first_name'))
                get_user.first_name = request.POST.get('first_name')
                get_user.save()
                messages.success(request, "First Name Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'last_name' in request.POST:
            try:
                edit_profile_form.fields["last_name"].validate(request.POST.get('last_name'))
                get_user.last_name = request.POST.get('last_name')
                get_user.save()
                messages.success(request, "Last Name Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'mobile' in request.POST:
            try:
                edit_profile_form.fields["mobile"].validate(request.POST.get('mobile'))
                get_user.mobile = request.POST.get('mobile')
                get_user.save()
                messages.success(request, "Mobile Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'email' in request.POST:
            try:
                edit_profile_form.fields["email"].validate(request.POST.get('email'))
                get_user.email = request.POST.get('email')
                get_user.save()
                messages.success(request, "Email Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'username' in request.POST:
            try:
                edit_profile_form.fields["username"].validate(request.POST.get('username'))
                get_user.username = request.POST.get('username')
                get_user.save()
                messages.success(request, "Username Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'injuries' in request.POST:
            try:
                edit_profile_form.fields["injuries"].validate(request.POST.get('injuries'))
                get_user.injuries = request.POST.get('injuries')
                get_user.save()
                messages.success(request, "Injuries Section Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif 'self_depict' in request.POST:
            try:
                edit_profile_form.fields["self_depict"].validate(request.POST.get('self_depict'))
                get_user.self_depict = request.POST.get('self_depict')
                get_user.save()
                messages.success(request, "User Additional Information Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        return render(request, "accounts/profile.html",{
            "get_user":get_user
        })
        
    else:
        return render(request, 'accounts/profile.html', {
            "get_user":get_user,
            "edit_profile_form": UserEditProfile()
        })


#to add a POST in order to do CRU_ on the user's profile
