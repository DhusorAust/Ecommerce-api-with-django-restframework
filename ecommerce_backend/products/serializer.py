from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
    


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        
        category_data = validated_data.pop('category')
        category_k = Category.objects.create(**validated_data)
        
        Product.objects.create(user=category_k, **category_data)
        return category_k