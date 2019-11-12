from django.shortcuts import render
from .models import Item
from payment.models import InvoiceItem
# Create your views here.

def shop(request):
    added = request.GET.get('added')
    items = Item.objects.filter()
    starter_check = False
    invoice_check = InvoiceItem.objects.filter(sku="000001")
    for item in invoice_check:
        if item.transaction.owner == request.user:
            starter_check = True
    return render(request, 'shop/shop.template.html',{
        "items":items,
        "starter_check": starter_check,
        'added': added
    })