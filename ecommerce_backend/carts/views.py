from itertools import product
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from .models import AddToCart

from .serializer import AddToCartSerializer
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.http.response import JsonResponse

from  rest_framework import generics

class CreatCart(APIView):
    def post(self,request):
        
        user = request.user
        
        data = request.data

        cart = AddToCart.objects.create(
                user = user,
                product  = data['product'],
                qty = data['qty'],
                price = data['price'],
                shippingPrice = data['shippingPrice']
            )
        
        cart.save()
    
        serializer=AddToCartSerializer(cart,many=False)
    
    
    
        return Response(serializer.data)
    
    
    



@api_view(['GET'])

def get_cart(request): 
    
    queryset=AddToCart.objects.all()

    serializer=AddToCartSerializer(queryset , many = True)
    return Response(serializer.data)