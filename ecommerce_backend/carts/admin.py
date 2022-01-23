from django.contrib import admin

# Register your models here.


from .models import AddToCart,ShippingAddress

admin.site.register(AddToCart)


admin.site.register(ShippingAddress)