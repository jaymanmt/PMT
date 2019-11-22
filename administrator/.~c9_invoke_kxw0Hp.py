from django.shortcuts import render, HttpResponse, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import auth, messages
from accounts.models import MyUser, ReferralCode
from payment.models import Transaction, InvoiceItem
from accounts.forms import UserEditProfile
from django.core.exceptions import ValidationError

def is_user(user):
    return user.groups.filter(name='user').exists()

def is_administrator(user):
    return user.groups.filter(name='administrator').exists()
    

# @user_passes_test(is_administrator) # or @user_passes_test(is_in_multiple_groups)
@login_required
def administrator_view(request):
    check_administrator = is_administrator(request.user)
    if check_administrator == True:
        all_users = MyUser.objects.filter().order_by("first_name")
        number_of_users = len(all_users)
        tx_with_charges = Transaction.objects.filter(charge__isnull=False)
        for all
        print(len(tx_with_charges))
        for tx in tx_with_charges:
            print('------------')
            print(tx)
        return render(request, 'administrator/administrator_page.html',{
            "all_users": all_users,
            "number_of_users":number_of_users
        })
    else:
        messages.error(request,'You do not have the permission to access this page')
        return render(request,'payment/oops.html')

def view_user(request, id):
    get_user = get_object_or_404(MyUser, pk=id)
    get_user_tx = Transaction.objects.filter(owner=id)
    
    if request.method == "POST":
        if 'delete_user' in request.POST:
            try:
                delete_user = get_object_or_404(MyUser, pk=id).delete()
            except ValidationError as e:
                return HttpResponse(e)
        return HttpResponseRedirect(reverse('administrator_view'))
    else:
        return render(request, "administrator/user_page.html",{
            "get_user": get_user,
            "get_user_tx":get_user_tx
        })

#function put into an action within a form to update a transaction's status from the user_page using the administrator's permissions.
def update_tx_status(request, id, tx_num):
    if 'edit_tx_status' in request.POST:
        get_user_tx = Transaction.objects.filter(owner=id)
        for tx in get_user_tx:
            if int(tx.id) == int(tx_num):
                tx.status = request.POST.get('tx_status')
                tx.save()

        return HttpResponseRedirect(reverse('administrator_view'))
    else:
        messages.error(request, 'Status could not be updated, something went wrong')
        return HttpResponseRedirect(reverse('administrator_view'))

def edit_user(request, id):
    get_user = get_object_or_404(MyUser, pk=id)
    # -------------- edit user's profile form ----------------
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
            
        return render(request, "accounts/profile.html")
        
    else:
        return render(request, 'accounts/profile.html', {
            "get_user":get_user,
            "edit_profile_form": UserEditProfile()
        })

def tx_user(request,tx_num):
    tx_invoice_item = InvoiceItem.objects.filter(transaction=tx_num)
    return render(request, "administrator/invoiceitems.html",{
        "tx_invoice_item":tx_invoice_item
    })

