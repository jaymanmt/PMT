from .models import Charge
from django import forms
from accounts.models import ReferralCode

class CheckRefCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        fields = (
            'discount',
        )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2'
        )

class PaymentForm(forms.Form):
    # use list comprehension to generate a list with tuples of months and years
    MONTH_CHOICES = [(i, i) for i in range(1, 12)] 
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)] 
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)