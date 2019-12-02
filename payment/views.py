from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.http import JsonResponse
import stripe
from django.conf import settings
from .forms import OrderForm, PaymentForm, CheckRefCodeForm
from basket.models import basketItem
from django.utils import timezone
from django.contrib import messages
from .models import Transaction, InvoiceItem
from shop.models import Item
from django.utils.crypto import get_random_string
from accounts.models import ReferralCode
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives

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
    
    return total_cost

#create url for AJAX call to check the referral code for user interface
def check_ref_code(request, ref_code):
    referral_codes = ReferralCode.objects.filter(discount=ref_code)
    if len(referral_codes) != 0 and referral_codes[0].expiry >= timezone.now() and referral_codes[0].active == True:
        return JsonResponse({"status":True})
    else:
        return JsonResponse({"status":False})

#function to pass into payment for backend
def check_ref_code_payment(request):
    ref_code = request.POST.get('ref_code')
    referral_codes = ReferralCode.objects.filter(discount=ref_code)
    if len(referral_codes) != 0 and referral_codes[0].expiry >= timezone.now() and referral_codes[0].active == True:
        try:
            referral_codes[0].active = False
            referral_codes[0].save()
        except ValidationError as e:
                return HttpResponse(e)
        return True
    else:
        return False

def pay_here(request):
    
    if request.method == 'GET':
        
        #total_cost_integer is what will be the amount in dollars that is calculated to be paid
        total_cost = calculate_bkt_cost(request)
        #total_cost_integer multiply amount to be paid into cents
        total_cost_integer = int(total_cost*100)
        if total_cost == 0:
            messages.error(request, "Your basket is empty, please add an item to proceed")
            return HttpResponseRedirect(reverse('showbasket'))
            
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
            # checking if there is enough stock before going to payment phase
            for stock in all_stock:
                if item.product.sku == stock.sku and item.quantity_to_buy > stock.stock_level:
                    messages.error(request, "Unfortunately, we are out of stock of {} for that quantity requested, please lower your quantity and try again, otherwise please contact us".format(item.product.product_name))
                    
                    return HttpResponseRedirect(reverse('showbasket'))
            # using elif for specific condition and breaking out of loop once a match is made comparing a basket item's quantity with a shop item's stock levels
                elif item.product.sku == stock.sku and item.quantity_to_buy <= stock.stock_level:
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
                    break

        
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
        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        
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
                    amount = int(request.POST['total_cost_for_payment'])
                    check_ref_code = check_ref_code_payment(request)
                    if check_ref_code == True:
                        amount = amount*0.9

                    customer = stripe.Charge.create(
                        amount = int(amount),
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
                        
                        transaction_charge_display= transaction.charge.amount / 100
                        transaction_charge_display = round(transaction_charge_display, 2)
                        payee_email= transaction.owner.email
                        
                        if transaction.owner == request.user: 
                            print(transaction.owner.first_name)
                            print(transaction.owner.last_name)
                            print(transaction.owner.email)
                            print(transaction.owner.mobile)
                            print(transaction.charge.amount)
                        subject = "Your Order has been received! "
                        text_content = """
Thank you for your prompt payment, this email is to confirm your order and payment of SGD {} on {}.
                        
Your limited time discount code is {}.
                        
You can refer a friend to receive that 10% off or use it yourself. It expires on {}.

I will be in contact with you within 1-2 business days to organise a suitable schedule, venue and timing with you.
                        
In the meantime, please update your profile on your account. The more information I have, the more effective I can design a personalised Muay Thai Training/Nutrition Session for you. 
                        
If you have any questions, feel free to get in contact with me at 8783 5456.
                        
Regards,
Jerald
Admin @PMTT
                        """.format(transaction_charge_display, transaction.charge.date, unique_code, expiry_date)
                        sender = "no-reply@mail.sgmuaythai.org"
                        payee = payee_email
                        msg = EmailMultiAlternatives(subject, text_content, sender, [payee])
                        msg.send()
                        
                        subject2 = "An Order has been received! "
                        text_content2 = """
This email confirms an order with payment of SGD {} on {}.

Customer Name: {} {}
Customer Email: {}
Customer Mobile: {}
Customer Address: {}, {}


Issued limited time discount code is {} and it expires on {}.

Please organise a suitable schedule, venue and timing with client within 1-2 business days.

Regards,
Admin @PMTT
                        """.format(transaction_charge_display, transaction.charge.date, transaction.owner.first_name, transaction.owner.last_name, transaction.owner.email, transaction.owner.mobile, transaction.charge.street_address1, transaction.charge.street_address2, unique_code, expiry_date)
                        sender2 = "no-reply@mail.sgmuaythai.org"
                        administrator = "jeraldtanxh@hotmail.com"
                        msg2 = EmailMultiAlternatives(subject2, text_content2, sender2, [administrator])
                        msg2.send()
                        
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

# order history pages

def orderhistory(request):
    user_transactions = Transaction.objects.filter(owner=request.user)
    return render(request, 'payment/orderhistory.html', {
        "user_transactions": user_transactions
    })

def orderhistory_tx(request, tx_id):
    user_transaction = Transaction.objects.get(owner=request.user, id=tx_id)
    invoice_items = InvoiceItem.objects.filter(transaction__owner=request.user, transaction__id=tx_id)
    return render(request, 'payment/orderhistory_tx.html', {
        "user_transaction":user_transaction,
        "tx_id":tx_id,
        "invoice_items":invoice_items
    })