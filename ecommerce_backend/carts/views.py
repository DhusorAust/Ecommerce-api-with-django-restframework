from traceback import print_exc
from django.shortcuts import render

# Create your views here.


from .models import AddToCart

from .serializer import AddToCartSerializer
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.http.response import JsonResponse


from rest_framework import viewsets

from products.models import Product


class CartViewSet(viewsets.ModelViewSet):
    
    queryset=AddToCart.objects.all()
    
    serializer_class= AddToCartSerializer




class CreateCartViewSet(viewsets.ModelViewSet):
    
    queryset=AddToCart.objects.all()
    
    serializer_class= AddToCartSerializer   
    
    
    def create(self, request):
        
        data=request.user.id
        
        cart=AddToCart.objects.create(

        user=request.user,
        
        product=Product.objects.get(pk=data['product']),
        
        qty=data['qty'],
        
        price=data['price'],
        
        shippingPrice=data['shippingPrice']
        

        )
        
        cart.save()
        
        return Response("created")
