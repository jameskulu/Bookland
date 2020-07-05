from django.urls import path
from Cart import views

urlpatterns = [
    path('', views.cart_detail, name='cart-detail'),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('update-cart/<int:id>', views.update_cart, name='update-cart'),
    path('remove-from-cart/<int:id>',
         views.remove_from_cart, name='remove-from-cart')
]
