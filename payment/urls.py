from django.urls import path
from .views import pay_here

urlpatterns = [
    path('', pay_here, name = 'pay_here')
]