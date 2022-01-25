from django.shortcuts import render


# Create your views here.

from .models import Category, Product
from .serializer import ProductSerializer

from rest_framework.response import Response


from django.shortcuts import render

from rest_framework import status


from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated,IsAdminUser



class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        
        data=request.data
        
        product=Product.objects.create(
            
            category=Category.objects.get(pk=data['category']),
            
            product_name=data['product_name'],
            
            price=data['price'],
            
            description=data['description'],
            stock=data['stock']
        
            
        )
        
        
        product.save()
        
        return Response("Created")






def get_permissions(self):
   
    if self.action == 'list':
        permission_classes = [IsAdminUser]
        
        
    elif self.action == 'create':
        
        permission_classes = [IsAdminUser]
        
    return [permission() for permission in permission_classes]
            











# @api_view(['GET'])

# def productList(request):
        
#     category = request.query_params.get('category')
#     if category:
#         queryset = Product.objects.filter(category__category_name =  category)
#     else:
#         queryset = Product.objects.all()
#     serializer = ProductSerializer(queryset , many = True)
#     return Response(serializer.data)



# @api_view(['POST'])

# def CreateProduct(request):
#     serializer = ProductSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
# class EventView(APIView):
    
#     def post(self, request): 
        
#         serializer = ProductSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 