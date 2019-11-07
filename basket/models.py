from django.db import models

# Create your models here.
class basketItem(models.Model):
    product = models.ForeignKey('shop.Item', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    quantity_to_buy = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return str(self.product) + " x " + str(self.quantity_to_buy)