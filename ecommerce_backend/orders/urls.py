from .views import  OrderViewSet 
from django.urls import path,include

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('orderview', OrderViewSet, basename='orderview')




urlpatterns = [
     path('', include(router.urls)),
   
]