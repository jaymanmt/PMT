from django import forms
from accounts.models import ReferralCode

class CheckRefCode(forms.Form):
    class Meta:
        model = ReferralCode
        fields = (
            'discount'
        )