
from .models import AddToCart
from rest_framework import serializers
from django.contrib.auth.models import User



class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'


# class ShippingAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingAddress
#         fields = '__all__'



