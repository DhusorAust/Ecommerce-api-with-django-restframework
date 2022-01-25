from django.shortcuts import render

from carts.models import AddToCart
from carts.serializer import AddToCartSerializer
from rest_framework.response import Response

from .models import Oders

# from carts.models import 


from django.db.models.query_utils import Q

# Create your views here.

from rest_framework import viewsets

class OrderViewSet(viewsets.ViewSet):
    
    
    def list(self, request):
        
        queryset = AddToCart.objects.filter(user=request.user.id).filter(is_ordered=False)
        # serializer = AddToCartSerializer(queryset, many=True)
        
        sum1=0
        
        for query in queryset:
            
            print(query.id)
            
            sum1+=query.price
            
        print("Total Price",sum1)
        
        
        return Response("Getting Value")
    
    
    def create(self, request):
        
        
        queryset = AddToCart.objects.filter(user=request.user.id).filter(is_ordered=False)
        # serializer = AddToCartSerializer(queryset, many=True)
        
        sum1=0
        
        for query in queryset:
            
            sum1+=query.price
            
        print("Total Price",sum1)        
        
        data=request.data
        
        order=Oders.objects.create(

        user=request.user,
        
        total_price=sum1,
        
        address=data['address'],
        city=data['city'],
        postalCode=data['postalCode'],

        )
        
        
        
    
        order.save()
        
        
        for query in queryset:
            
            post = AddToCart.objects.get(id=query.id)
            
            post.is_ordered = True
            post.save()
    
        return Response("Ordered")