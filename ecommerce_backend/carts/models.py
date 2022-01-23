from django.db import models
from django.contrib.auth.models import User
from django.db.models import deletion

from products.models import Product




class AddToCart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
    
    qty = models.IntegerField(default=0, blank=True, null=True)
    
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    
    _id = models.AutoField(primary_key=True, editable=False)
    
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

class ShippingAddress(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postalCode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
