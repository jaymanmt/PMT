from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
import stripe
from django.conf import settings
from .forms import OrderForm, PaymentForm, CheckRefCode
from basket.models import basketItem
from django.utils import timezone
from django.contrib import messages
from .models import Transaction, InvoiceItem
from shop.models import Item
from django.utils.crypto import get_random_string
from accounts.models import ReferralCode

# Create your views here.
if request.method == 'POST':
        pass
        # try:
        #     check_ref_form = CheckRefCode({
        #     "discount":request.POST.get('ref_code')
        #     })
        #     check_ref_form.fields["discount"].validate(request.POST.get('ref_code'))
        #     print('validation success!---------------')
        # except ValidationError as e:
        #         return HttpResponse(e)
        ref_code_submitted = request.POST.get('ref_code')
        check_ref_code = MyUser.objects.get(referral_code=ref_code_submitted)
        if check_ref_code != None:
            edit_ref_code = ReferralCode.objects.get(discount=check_ref_code)
            if edit_ref_code.active == True and edit_ref_code.expiry <= timezone.now():
                # activate discount
                edit_ref_code.active = False
                edit_ref_code.save()
            else:
                messages.error(request, 'oops! The discount code is invalid')
                
        return HttpResponseRedirect(reverse('showbasket'))

#function to calculate total cost in basket of the current user 
def calculate_bkt_cost(request):

    total_cost = 0
    number_of_items = 0
    all_basket_items = basketItem.objects.filter(owner=request.user)
    for each_item in all_basket_items:
        number_of_items+= each_item.quantity_to_buy
        total_cost+=each_item.calculate_total()
    
    if number_of_items >= 5:
        total_cost = total_cost * 0.9
    
    
    
    #call and check 10, 20, 30, 40% off referral codes status, and if any are active, do the discount followed by changing the status back to inactive 
    # dj2938f7hkd0j10
    # 9dj342khbazmh20
    # gas2310h4kamt30
    
    return total_cost

def pay_here(request):
    
    if request.method == 'GET':
        #total_cost_integer is what will be the amount in dollars that is calculated to be paid
        total_cost = calculate_bkt_cost(request)
        #total_cost_integer multiply amount to be paid into cents
        total_cost_integer = int(total_cost*100)
        if total_cost == 0:
            messages.error(request, "Your basket is empty, please add an item to proceed")
            return render(request, 'payment/oops.html')
            
        #convert to two decimal places string
        total_cost = "{:.2f}".format(total_cost)
        #prevents the pending transactions from being created over and over again from page refreshes 
        delete_previous_transactions = Transaction.objects.filter(owner=request.user,status='pending').delete()
        
        transaction = Transaction()
        transaction.owner = request.user
        transaction.status = 'pending'
        transaction.date = timezone.now()
        
        transaction.save()
        
        basket_items = basketItem.objects.filter(owner=request.user)
        all_stock = Item.objects.filter()
        for item in basket_items:
            # checking if there is enough stock and if it is sold out
            for stock in all_stock:
                if item.product.sku == stock.sku and item.quantity_to_buy > stock.stock_level:
                    messages.error(request, "Unfortunately, we are out of stock of {} for that quantity requested, please lower your quantity and try again, otherwise please contact us".format(item.product.product_name))
                    #send an email to admin??
                    return HttpResponseRedirect(reverse('showbasket'))
                else:
                    invoice_item = InvoiceItem()
                    invoice_item.transaction = transaction
                    invoice_item.product = item.product
                    invoice_item.quantity = item.quantity_to_buy
                    if item.quantity_to_buy >=5:
                        price_to_discount = item.product.price
                        invoice_item.price = price_to_discount*0.9
                    else:
                        invoice_item.price = item.product.price * item.quantity_to_buy
                    invoice_item.sku = item.product.sku
                    invoice_item.name = item.product.product_name
                    
                    invoice_item.save()
        
        order_form = OrderForm()
        payment_form = PaymentForm()

        
        return render(request, 'payment/paying.html', {
            "total_cost":total_cost,
            "total_cost_integer":total_cost_integer,
            "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
            "order_form": order_form,
            "payment_form":payment_form,
            "transaction":transaction
        })
    else:
        
        
        # check for status of particular transaction is not pending, if its anything apart from pending, it should have been paid for
        if transaction.status != 'pending':
            messages.error(request, "It seems like you have already made payment for this. Please check your bank account")
            return render(request, 'payment/oops.html')
            
        else:
            
            #stripe id is retrieved from the forms through a hidden widget
            stripeToken = request.POST['stripe_id']
            
            # set the secret key for the Stripe API
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            order_form = OrderForm(request.POST)
            payment_form = PaymentForm(request.POST)
            
            if order_form.is_valid() and payment_form.is_valid():
                
                try:
                    amount = 0
                    amount = request.POST['total_cost_for_payment']

                    customer = stripe.Charge.create(
                        amount = amount,
                        currency='sgd',
                        description='Stripe Payment Form',
                        card=stripeToken
                        )
                        
                    if customer.paid:
                        # generate and assign a new referral code to every new purchase
                        unique_code = get_random_string(length=10)
                        all_ref_codes = ReferralCode.objects.filter()
                        for code in all_ref_codes:
                            while unique_code == code:
                                unique_code = get_random_string(length=10)
                        
                        new_code = ReferralCode()
                        
                        new_code.discount = unique_code
                        new_code.active = True
                        new_code.expiry = timezone.now() + timezone.timedelta(days=22)
                        expiry_date = timezone.now() + timezone.timedelta(days=22)
                        new_code.save()
                        order = order_form.save(commit=False)
                        order.amount = amount
                        order.date=timezone.now()
                        order.save()
                        transaction.status = 'approved'
                        transaction.charge = order
                        transaction.save()
                        
                        #updating stock levels of the shop
                        invoice_items = InvoiceItem.objects.filter(transaction_id=transaction.id)
                        for each_item in invoice_items:
                            if each_item.product.stock_level >= 0:
                                each_item.product.stock_level -= each_item.quantity
                                each_item.product.save()
                            else:
                                messages.error(request, 'unfortunately, the requested item(s) is out of stock. Please get in contact with us to resolve this.')
                            
                        #empty the user's shop basket
                        basket_items = basketItem.objects.filter(owner = request.user).delete()
                        return render(request, 'payment/thankyou.html',{
                            "unique_code":unique_code,
                            "expiry_date":expiry_date
                        })
                    else:
                        messages.error(request, "Your card has been declined")
                        return render(request, 'payment/oops.html')
                except stripe.error.CardError:
                    messages.error(request, "Payment was unsuccessful, please check your card details")
                    return render(request, 'payment/oops.html')
            else:
                messages.error(request, "An error has occured while processing your payment, please fill in the form again")
                return render(request, 'payment/paying.html', {
                'order_form' : order_form,
                'payment_form' : payment_form,
                'total_cost' : total_cost,
                "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY
            })
            
            return render(request, 'payment/paying.html', {
                'order_form' : order_form,
                'payment_form' : payment_form,
                'total_cost' : total_cost,
                "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY
                })

# order history page

def orderhistory(request):
    invoice_items = InvoiceItem.objects.filter(transaction__owner=request.user)
    
    return render(request, 'payment/orderhistory.html', {
        "invoice_items": invoice_items
    })