from django.urls import path
from .views import pay_here, orderhistory, check_ref_code, orderhistory_tx

urlpatterns = [
    path('', pay_here, name = 'pay_here'),
    path('orderhistory', orderhistory, name='orderhistory'),
    path('orderhistory/<tx_id>', orderhistory_tx, name='orderhistory_tx'),
    path('check_ref_code/<ref_code>', check_ref_code, name="check_ref_code")
]