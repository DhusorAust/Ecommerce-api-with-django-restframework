from django.urls import path,include

from . import views

from .views import  CartViewSet 

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('cartview', CartViewSet, basename='cartview')




urlpatterns = [
     path('', include(router.urls)),
   
]


