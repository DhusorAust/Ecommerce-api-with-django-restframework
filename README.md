# Ecommerce-api-with-django-restframework

* It is Rest API based django project
* jwt authentications are used for the registration and login
* every user get an access key for doing other functional work
* only admin can create products
* user can add any products to cart with quantity number.And receiver decorator function multiply the product pricess with quantity and also add shipping cost
* user can see all the cart list that added before. is_ordered boolean field is initially False. 
* order app calculate all the carts prices calculate total price and set cart is_ordered boolean field to True. 
* order app saves all the information with shipping address.

*** In future I will try to Add payment methods for this project and also try to build Front-END for the this project. 
