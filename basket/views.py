from django.shortcuts import render, redirect, reverse
from .models import basketItem
from shop.models import Item
# Create your views here.
def showbasket(request):
    total_cost = 0
    all_basket_items = basketItem.objects.filter(owner=request.user)
    for each_item in all_basket_items:
        total_cost+=each_item.product.price * each_item.quantity_to_buy
    
    total_cost = total_cost/100
    return render(request, "basket/basket_view.template.html", {
        "all_basket_items":all_basket_items,
        "total_cost":total_cost
    })
    
def addtobasket(request, product_id):
    # determine which product we are buying
    product = Item.objects.get(pk=product_id)
    
    # if the product already exists in the user's shopping basket
    existing_bkt_item = basketItem.objects.filter(owner=request.user, product=product).first()
    
    # if the basket item does not exist, create new one
    if existing_bkt_item == None:
        new_bkt_item = basketItem()
        new_bkt_item.product = product
        new_bkt_item.owner = request.user
        new_bkt_item.quantity_to_buy = 1
        new_bkt_item.save()
    else:
        # increases its quantity
        existing_bkt_item.quantity_to_buy += 1
        existing_bkt_item.save()
    return redirect(reverse('shop'))

def removefrombasket(request, bkt_item_id):
    existing_bkt_item = basketItem.objects.get(pk=bkt_item_id)
    existing_bkt_item.delete()
    return redirect(reverse('shop'))