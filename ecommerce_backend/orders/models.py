from django.db import models

# Create your models here.
from django.db import models

from carts.models import AddToCart
from django.dispatch import receiver
from django.contrib.auth.models import User



class Oders(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # cart=models.ForeignKey(AddToCart, on_delete=models.CASCADE, null=True)
    
    total_price=models.IntegerField(default=0, blank=True, null=True)

    
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postalCode = models.CharField(max_length=200, blank=True, null=True)
    




