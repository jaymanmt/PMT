from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    first_name= models.CharField(max_length=80, blank=False, default="")
    last_name= models.CharField(max_length=80, blank=False, default="")
    email = models.CharField(max_length=80, blank=False, default="")
    injuries = models.TextField(max_length=1000, blank=True, default="")
    mobile = models.CharField(max_length=50, blank=False, default="")
    def __str__(self):
        return str(self.username)