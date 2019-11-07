from django.shortcuts import render
from .models import Item
# Create your views here.

def shop(request):
    items = Item.objects.filter()
    return render(request, 'shop/shop.template.html',{
        "items":items
    })