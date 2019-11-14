from .models import basketItem


def basketcount(request):
    total_quantity = 0
    if request.user.is_authenticated:
        basketcounter = basketItem.objects.filter(owner=request.user)
        for each_item in basketcounter:
            total_quantity+=each_item.quantity_to_buy
        return {
            "total_quantity":total_quantity
        }
    else:
        return {}
    
    
