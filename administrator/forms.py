from django import forms
from shop.models import Item
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['product_name','sku','sessions','description','price','stock_level','category', 'photo', 'sold_out']