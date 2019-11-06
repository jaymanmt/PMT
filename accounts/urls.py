from django.urls import path
from .views import home, logout, login, register, user_profile, partner

urlpatterns = [
    path('', home, name="home"),
    path('logout', logout, name='logout'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', user_profile, name="profile"),
    path('partner', partner, name='partner'),
]