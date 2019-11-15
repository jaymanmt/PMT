from django.contrib import admin
from .models import MyUser, ReferralCode
# Register your models here.
admin.site.register(MyUser)
admin.site.register(ReferralCode)