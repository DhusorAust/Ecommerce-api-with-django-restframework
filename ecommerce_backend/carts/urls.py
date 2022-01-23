from django.urls import path

from . import views


urlpatterns = [
      path('createcart/', views.CreatCart.as_view(), name='carts_c'),
      path('getcart/', views.get_cart, name='carts_g'),

   
]


