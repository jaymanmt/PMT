from django.db import models

# Create your models here.
class basketItem(models.Model):
    product = models.ForeignKey('shop.Item', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    quantity_to_buy = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return str(self.owner) + " - " + str(self.product) + "x" + str(self.quantity_to_buy)
# calculate the 10% discount if the quantity of a particular  basket item is above 5. 
    def calculate_total(self):
        new_cost = (self.quantity_to_buy*self.product.price)/100
        return int(new_cost)
