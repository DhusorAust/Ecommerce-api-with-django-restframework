
from django.urls import path,include

from . import views




from .views import  ProductViewSet 

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('product', ProductViewSet, basename='product')



urlpatterns = [
    
    
    path('', include(router.urls)),

]


