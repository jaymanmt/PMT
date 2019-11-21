from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone


# Create your models here.
def three_weeks_later():
    return timezone.now() + timezone.timedelta(days=21)
    
class MyUser(AbstractUser):
    first_name= models.CharField(max_length=80, blank=False, default="")
    last_name= models.CharField(max_length=80, blank=False, default="")
    mobile = models.CharField(max_length=50, blank=False, default="")
    email = models.CharField(max_length=80, blank=False, default="")
    self_depict = models.TextField(max_length=1000, blank=True, default="")
    injuries = models.TextField(max_length=1000, blank=True, default="")
    photo = models.ImageField(upload_to='static/images/', null=True)
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.username)
    
class ReferralCode(models.Model):
    discount = models.CharField(max_length=15, blank=False, default="")
    expiry = models.DateTimeField(default=three_weeks_later)
    active = models.BooleanField(blank=False, null=True)
    
    
    def __str__(self):
        return str(self.active) + ", expires on " + str(self.expiry)