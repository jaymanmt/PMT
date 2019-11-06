from django.db import models

# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=80, blank=False)
    sku = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=1000, blank=True, default="")
    price = models.CharField(max_length=50, blank=False)
    stock_level = models.IntegerField(blank=False)
    sold_out = models.BooleanField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/images/', null=True)
    def __str__(self):
        return self.product_name

class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return self.name