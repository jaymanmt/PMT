from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import auth, messages


def is_user(user):
    return user.groups.filter(name='user').exists()

def is_administrator(user):
    return user.groups.filter(name='administrator').exists()
    

# @user_passes_test(is_administrator) # or @user_passes_test(is_in_multiple_groups)
@login_required
def administrator_view(request):
    check_administrator = is_administrator(request.user)
    if check_administrator == True:
        return render(request, 'administrator/administrator_page.html')
    else:
        messages.error(request,'You do not have the permission to access this page')
        return render(request,'payment/oops.html')