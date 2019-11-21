from django.urls import path
from .views import administrator_view

urlpatterns = [
    path('',administrator_view, name="administrator_view")
]