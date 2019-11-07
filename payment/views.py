from django.shortcuts import render, HttpResponse
import stripe
from django.conf import settings
from .forms import OrderForm, PaymentForm
from basket.models import basketItem
from django.utils import timezone
from django.contrib import messages

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
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'payment/paying.html', {
            "total_cost":total_cost/100,
            "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
            "order_form": order_form,
            "payment_form":payment_form
        })
    else:
        #stripe id is part of forms with a hidden widget
        stripeToken = request.POST['stripe_id']
        
        # set the secret key for the Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                amount=0
                old_amount= float(request.POST['total_cost']),
                amount= round(amount,2) * 100,
                customer = stripe.Charge.create(
                    amount = amount,
                    currency='sgd',
                    description='Payment',
                    card=stripeToken
                    )
                    
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
                    
                    return render(request, 'payment/thankyou.html')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
            
        else:
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