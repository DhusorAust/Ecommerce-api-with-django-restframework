from django.db import models
from django.contrib.auth.models import User
from django.db.models import deletion

from products.models import Product

from django.db.models.signals import pre_save,post_save

from django.dispatch import receiver

class AddToCart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True) 
    
    qty = models.IntegerField(default=0, blank=True, null=True)
        
    shippingPrice = models.IntegerField(default=100, blank=True, null=True)

    price=models.IntegerField(default=0, blank=True, null=True)
    
    is_ordered=models.BooleanField(default=False)



@receiver(pre_save, sender=AddToCart)
def calculate_price(sender, **kwargs):
    
    obj=kwargs['instance']
    
    price_product=Product.objects.get(id=obj.product.id)
    
    obj.price=(obj.qty * int(price_product.price)) +  obj.shippingPrice
    
    
    return obj





class ShippingAddress(models.Model):
    
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postalCode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)
