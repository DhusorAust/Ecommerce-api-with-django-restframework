
from django.urls import path

from . import views

from .views import EventView


urlpatterns = [
   path('products/', views.productList, name='products'),
   
      path('create_product/', EventView.as_view(), name='products_'),

]