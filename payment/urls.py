from django.urls import path
from .views import ask_pay, pay_here

urlpatterns = [
    path('', ask_pay, name="pay"),
    path('stripepay', pay_here, name = 'pay_here')
]