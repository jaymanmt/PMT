from django import forms
from shop.models import Item
class UpdateItemForm(forms.Form):
    class Meta:
        model = Item
        fields = ['product_name','sku','sessions','description','price','category', 'photo']