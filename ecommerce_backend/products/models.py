from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name



class Product(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    product_name = models.CharField(max_length=100,blank=True, null=True)
    price = models.CharField(max_length=20,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=100)
    _id = models.AutoField(primary_key=True, editable=False)
    
    class Meta:
        pass
        
    
    def __str__(self):
        return self.product_name
    
    
    
    