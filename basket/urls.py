from django.urls import path
from .views import showbasket

urlpatterns = [
    path('', showbasket, name='showbasket')
]