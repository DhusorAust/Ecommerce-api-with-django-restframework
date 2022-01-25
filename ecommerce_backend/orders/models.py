from django.db import models

# Create your models here.
from django.db import models

from carts.models import AddToCart
from django.dispatch import receiver
 


class Oders(models.Model):
    
    cart=models.ForeignKey(AddToCart, on_delete=models.CASCADE, null=True)
    
    
    
    pass




