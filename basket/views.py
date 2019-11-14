from django.shortcuts import render, redirect, reverse
from .models import basketItem
from shop.models import Item

# Show basket function
def showbasket(request):
    
    each_item_total_cost = 0
    total_cost = 0
    number_of_bkt_items = 0
    
    all_basket_items = basketItem.objects.filter(owner=request.user)
    for each_item in all_basket_items:
        number_of_bkt_items+=1
        total_cost+=each_item.calculate_total()

    return render(request, "basket/basket_view.template.html", {
        "all_basket_items":all_basket_items,
        "total_cost":total_cost,
        "number_of_bkt_items":number_of_bkt_items
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
    return redirect(reverse('shop')+'?added=1')

def addtobasketfrombasket(request, product_id):
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
    return redirect(reverse('showbasket')+'?added=1')

def removefrombasketfrombasket(request, product_id):
    # determine which product we are buying
    product = Item.objects.get(pk=product_id)
    
    # if the product already exists in the user's shopping basket
    existing_bkt_item = basketItem.objects.filter(owner=request.user, product=product).first()
    
    # decreases its quantity
    existing_bkt_item.quantity_to_buy -= 1
    existing_bkt_item.save()
    return redirect(reverse('showbasket')+'?added=1')
    
def removefrombasket(request, bkt_item_id):
    existing_bkt_item = basketItem.objects.filter(pk=bkt_item_id)
    for each_bkt_item in existing_bkt_item:
        each_bkt_item.delete()
    return redirect(reverse('showbasket'))