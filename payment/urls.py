from django.urls import path
from .views import pay_here, orderhistory

urlpatterns = [
    path('', pay_here, name = 'pay_here'),
    path('orderhistory', orderhistory, name='orderhistory')
]