from django.shortcuts import render, HttpResponse
import stripe
from django.conf import settings
from .forms import OrderForm, PaymentForm
from basket.models import basketItem
from django.utils import timezone
from django.contrib import messages
from .models import Transaction, InvoiceItem

# Create your views here.

def calculate_bkt_cost(request):
    basket_items = basketItem.objects.filter(owner = request.user)
    amount = 0
    for item in basket_items:
        amount += item.product.price* item.quantity_to_buy
    return amount


def pay_here(request):
    
    if request.method == 'GET':
        total_cost = calculate_bkt_cost(request)
        total_cost_in_dollars = round(total_cost/100, 2)
        if total_cost == 0:
            return HttpResponse('empty basket')
        
        #prevents the empty transactions from being created over and over again from page refreshes 
        delete_previous_transactions = Transaction.objects.filter(owner=request.user).delete()
        transaction = Transaction()
        transaction.owner = request.user
        transaction.status = 'pending'
        transaction.date = timezone.now()
        
        transaction.save()
        
        basket_items = basketItem.objects.filter(owner=request.user)
        for item in basket_items:
            invoice_item = InvoiceItem()
            invoice_item.transaction = transaction
            invoice_item.product = item.product
            invoice_item.quantity = item.quantity_to_buy
            invoice_item.sku = item.product.sku
            invoice_item.name = item.product.product_name
            invoice_item.price = item.product.price
            invoice_item.save()
        
        
        
        order_form = OrderForm()
        payment_form = PaymentForm()
        
        return render(request, 'payment/paying.html', {
            "total_cost":total_cost,
            "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
            "order_form": order_form,
            "payment_form":payment_form,
            "total_cost_in_dollars":total_cost_in_dollars,
            "transaction":transaction
        })
    else:

        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        if transaction.status != 'pending':
            return HttpResponse('payment has already been made, please check your bank account')
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
                    amount = request.POST['total_cost']

                    customer = stripe.Charge.create(
                        amount = amount,
                        currency='sgd',
                        description='Stripe Payment Form',
                        card=stripeToken
                        )
                        
                    if customer.paid:
                        
                        order = order_form.save(commit=False)
                        order.date=timezone.now()
                        order.save()
                        transaction.status = 'approved'
                        transaction.charge = order
                        transaction.save()
                        
                        #updating stock levels of the shop
                        invoice_items = InvoiceItem.objects.filter(transaction_id=transaction.id)
                        for each_item in invoice_items:
                            each_item.product.stock_level -= each_item.quantity
                            each_item.product.save()
                            
                        #empty the user's shop basket
                        basket_items = basketItem.objects.filter(owner = request.user).delete()
                        return render(request, 'payment/thankyou.html')
                    else:
                        messages.error(request, "Your card has been declined")
                except stripe.error.CardError:
                        messages.error(request, "Payment was unsuccessful, please check your card details!")
                
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