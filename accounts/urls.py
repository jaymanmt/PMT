from django.urls import path
from .views import home, logout, login, register, edit_profile, partner

urlpatterns = [
    path('', home, name="out"),
    path('logout', logout, name='logout'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile/<id>', edit_profile, name="edit_profile"),
    path('partner', partner, name='partner'),
]