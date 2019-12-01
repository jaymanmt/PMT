from django.shortcuts import render
from .models import Item
from payment.models import InvoiceItem
from basket.models import basketItem
# Create your views here.

def shop(request):
    items = Item.objects.filter().order_by('price')
    
    if request.user.is_authenticated:
        #make sure that the starter's package can only be bought once by each user
        bkt_starter_bool = True
        bkt_check_starter = basketItem.objects.filter(owner=request.user)
        for basket_item in bkt_check_starter:
            if basket_item.product.sku == '000001':
                bkt_starter_bool = False
        
        added = request.GET.get('added')
        
        starter_check = False
        invoice_check = InvoiceItem.objects.filter(sku="000001")
        for item in invoice_check:
            if item.transaction.owner == request.user:
                starter_check = True
        return render(request, 'shop/shop.template.html',{
                "items":items,
                "starter_check": starter_check,
                'added': added,
                'bkt_starter_bool': bkt_starter_bool
            })
    else:
        return render(request, 'shop/shop.template.html',{
            "items":items,
        })