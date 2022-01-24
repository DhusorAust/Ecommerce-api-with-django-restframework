from traceback import print_exc
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User


from .models import AddToCart

from .serializer import AddToCartSerializer
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.http.response import JsonResponse


from rest_framework import viewsets

from products.models import Product

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated,IsAdminUser


from rest_framework.decorators import action

# class CartViewSet(viewsets.ModelViewSet):
    
#     queryset=AddToCart.objects.get(id=request.user.id)
    
#     serializer_class= AddToCartSerializer




class CartViewSet(viewsets.ViewSet):
    
    permission_classes=[IsAdminUser] 
    
    def list(self, request):
        
        queryset = AddToCart.objects.filter(id=request.user.id)
        serializer = AddToCartSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        data=request.data
        
        cart=AddToCart.objects.create(

        user=request.user,
        
        product=Product.objects.get(pk=data['product']),
        
        qty=data['qty']
        

        )
        
        cart.save()
        
        return Response("created")

def get_permissions(self):
   
    if self.action == 'list':
        permission_classes = [IsAuthenticated]
        
        
    elif self.action == 'create':
        
        permission_classes = [IsAdminUser]
        
    return [permission() for permission in permission_classes]
            