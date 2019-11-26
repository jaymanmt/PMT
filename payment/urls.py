from django.urls import path
from .views import pay_here, orderhistory, check_ref_code

urlpatterns = [
    path('', pay_here, name = 'pay_here'),
    path('orderhistory', orderhistory, name='orderhistory'),
    path('check_ref_code/<ref_code>', check_ref_code, name="check_ref_code")
]