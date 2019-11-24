from django.shortcuts import render, HttpResponse, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.contrib import auth, messages
from accounts.models import MyUser, ReferralCode
from payment.models import Transaction, InvoiceItem, Charge
from shop.models import Item, Category
from accounts.forms import UserEditProfile
from django.core.exceptions import ValidationError
from .forms import UpdateItemForm

def is_user(user):
    return user.groups.filter(name='user').exists()

def is_administrator(user):
    return user.groups.filter(name='administrator').exists()
    

# @user_passes_test(is_administrator) # or @user_passes_test(is_in_multiple_groups)
@login_required
def administrator_view(request):
    check_administrator = is_administrator(request.user)
    if check_administrator == True:
        #update sold out status if stock level is 0 and below when admin logs in 
        stock = Item.objects.filter()
        for item in stock:
            if item.stock_level <= 0:
                item.sold_out = True
                item.save()
            elif item.stock_level >= 0:
                item.sold_out = False
                item.save()
                
        number_of_customer = 0
        all_users = MyUser.objects.filter().order_by("first_name")
        number_of_users = len(all_users)
        tx_with_charges = Transaction.objects.filter(charge__isnull=False)
        all_tx = Transaction.objects.filter()
        tx_without_charges = len(all_tx) - len(tx_with_charges)
        for user in all_users:
            for txc in tx_with_charges:
                if str(txc.owner) == str(user.username):
                    number_of_customer+=1
                    break
                else:
                    continue
        all_tx = len(all_tx)
        conversion_rate = (int(number_of_customer) / int(number_of_users) ) * 100
        conversion_rate = round(conversion_rate, 2)
        
        tx_pending = Transaction.objects.filter(status='pending')
        tx_pending = len(tx_pending)
        
        tx_approved = Transaction.objects.filter(status='approved')
        tx_approved = len(tx_approved)
        
        tx_delivered = Transaction.objects.filter(status='delivered')
        tx_delivered = len(tx_delivered)
        
        tx_lost = Transaction.objects.filter(status='lost')
        tx_lost = len(tx_lost)
        
        tx_shipping = Transaction.objects.filter(status='shipping')
        tx_shipping = len(tx_shipping)
        
        tx_rejected = Transaction.objects.filter(status='rejected')
        tx_rejected = len(tx_rejected)
        
        #get amount earned from Charge model
        get_charge = Charge.objects.filter()
        amount_earned = 0
        for each_charge in get_charge:
            amount_earned+=int(each_charge.amount)
        amount_earned_in_dollars = amount_earned/100
        amount_earned_in_dollars = round(amount_earned_in_dollars, 2)
        
        #get amount earned and quantity sold from InvoiceItem model for each product
        all_products_sold = InvoiceItem.objects.filter()
        starter_sold = InvoiceItem.objects.filter(sku='000001')
        beginner_sold = InvoiceItem.objects.filter(sku='000002')
        intermediate_sold = InvoiceItem.objects.filter(sku='000003')
        advanced_sold = InvoiceItem.objects.filter(sku='000004')
        
        all_products_sold = len(all_products_sold)
        starter_sold = len(starter_sold)
        beginner_sold = len(beginner_sold)
        intermediate_sold = len(intermediate_sold)
        advanced_sold = len(advanced_sold)
        
        #get shop items stock levels
        stock = Item.objects.filter()

        
        return render(request, 'administrator/administrator_page.html',{
            "all_users": all_users,
            "number_of_users":number_of_users,
            "number_of_customer":number_of_customer,
            "conversion_rate":conversion_rate,
            "all_tx":all_tx,
            "tx_without_charges":tx_without_charges,
            "tx_pending":tx_pending,
            "tx_approved":tx_approved,
            "tx_delivered":tx_delivered,
            "tx_lost":tx_lost,
            "tx_shipping":tx_shipping,
            "tx_rejected":tx_rejected,
            "amount_earned_in_dollars":amount_earned_in_dollars,
            "all_products_sold":all_products_sold,
            "starter_sold":starter_sold,
            "beginner_sold":beginner_sold,
            "intermediate_sold":intermediate_sold,
            "advanced_sold":advanced_sold,
            "stock":stock
            
            
            
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

#function to add or subtract stock levels of each shop item from admin dashboard, also include adding if the stock has been sold out
def update_stock(request):
    shop_stock = Item.objects.filter()
    if request.method == 'POST':

        if '000001' in request.POST:
            selected_stock = Item.objects.get(sku='000001')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000002' in request.POST:
            selected_stock = Item.objects.get(sku='000002')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000003' in request.POST:
            selected_stock = Item.objects.get(sku='000003')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000004' in request.POST:
            selected_stock = Item.objects.get(sku='000004')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000005' in request.POST:
            selected_stock = Item.objects.get(sku='000005')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000006' in request.POST:
            selected_stock = Item.objects.get(sku='000006')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000007' in request.POST:
            selected_stock = Item.objects.get(sku='000007')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000008' in request.POST:
            selected_stock = Item.objects.get(sku='000008')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        elif '000009' in request.POST:
            selected_stock = Item.objects.get(sku='000009')
            selected_stock.stock_level = request.POST.get("new_stock_level")
            selected_stock.save()
        
        else:
            messages.error(request, 'sorry, was unable to update due to an error')
        #update sold out status if stock level is 0 and below
        for item in shop_stock:
            if item.stock_level <= 0:
                item.sold_out = True
                item.save()
            elif item.stock_level >= 0:
                item.sold_out = False
                item.save()
    else:
        
        stock = Item.objects.filter()
        
    return render(request, "administrator/shop_detail.html",{
        "shop_stock":shop_stock
    })


#function to put into an action within a form to update a transaction's status from the user_page using the administrator's permissions.
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

def edit_shop_item(request, select_sku):
    shop_item = Item.objects.get(sku=select_sku)
    category = Category.objects.filter()
    
    if request.method == "POST":
        
        edit_item_form = UpdateItemForm({
            "product_name": request.POST.get("product_name"),
            "sku":request.POST.get("sku"),
            "sessions":request.POST.get("sessions"),
            "description":request.POST.get("description"),
            "price": request.POST.get("price"),
            "category": request.POST.get("product_name"),
            "photo": request.FILES.get("photo")
        })
    
        if "product_name" in request.POST:
            try:
                # edit_item_form.fields["product_name"].validate(request.POST.get('product_name'))
                shop_item.product_name = request.POST.get('product_name')
                shop_item.save()
                messages.success(request, "Product Name Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif "sku" in request.POST:
            try:
                # edit_item_form.fields["sku"].validate(request.POST.get('sku'))
                shop_item.sku = request.POST.get('sku')
                shop_item.save()
                messages.success(request, "Product SKU Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif "description" in request.POST:
            try:
                # edit_item_form.fields["description"].validate(request.POST.get('description'))
                shop_item.description = request.POST.get('description')
                shop_item.save()
                messages.success(request, "Product Number of Sessions Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif "price" in request.POST:
            try:
                # edit_item_form.fields["sessions"].validate(request.POST.get('price'))
                shop_item.price = request.POST.get('price')
                shop_item.save()
                messages.success(request, "Product Price Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
        elif "category" in request.POST:
            try:
                # edit_item_form.fields["category"].validate(request.POST.get('category'))
                chosen_category = Category.objects.get(name=request.POST.get('category'))
                shop_item.category = chosen_category
                shop_item.save()
                messages.success(request, "Product Category Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
                
        elif "photo" in request.FILES:
            try:
                # edit_item_form.fields["photo"].validate(request.FILES.get('photo'))
                shop_item.photo = request.FILES.get('photo')
                shop_item.save()
                messages.success(request, "Product Image Updated Successfully")
            except ValidationError as e:
                return HttpResponse(e)
    else:
        pass
    
    
    
    return render(request, 'administrator/edit_shop_item.html',{
    "edit_item_form":UpdateItemForm(),
    "shop_item":shop_item,
    "category":category
})
    
    
