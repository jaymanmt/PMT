from django.db import models

# Create your models here.
class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    amount = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.full_name, self.date)
        
class Transaction(models.Model):
    status_options = [
        ('pending','Pending'),
        ('rejected','Rejected'),
        ('delivered','Delivered'),
        ('lost', 'Lost'),
        ('approved','Approved'),
        ('shipping','Shipping')
        ]
    charge = models.ForeignKey('Charge', on_delete=models.CASCADE, null=True)
    status = models.CharField(blank=False, choices = status_options, max_length=50)
    date = models.DateField()
    owner = models.ForeignKey('accounts.MyUser', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return 'Tx No. ' + str(self.id)

class InvoiceItem(models.Model):
    product = models.ForeignKey('shop.Item', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=False)
    sku = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    name = models.CharField(max_length=200, blank=False)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    def __str__(self):
        return 'Part of Transaction No. ' + str(self.transaction)
    
    #calculate the 10% discount if the quantitiy of a basket item is above 5. 
    def calculate_total(self):
        if self.quantity_to_buy >= 5:
            discounted_cost = ((self.quantity_to_buy*self.product.price)/100)*0.9
            return int(discounted_cost)
        else:
            new_cost = (self.quantity_to_buy*self.product.price)/100
            return int(new_cost)