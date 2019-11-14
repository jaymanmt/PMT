from django.urls import path
from .views import showbasket, addtobasket, removefrombasket, addtobasketfrombasket

urlpatterns = [
    path('', showbasket, name='showbasket'),
    path('add-item-to-basket/<product_id>', addtobasket, name="addtobasket"),
    path('remove-item-from-basket/<bkt_item_id>', removefrombasket, name="removefrombasket"),
    path('add-item-to-basket-from-basket/<product_id>', addtobasketfrombasket, name="addtobasketfrombasket"),
]