from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/<int:pk>', views.product_detail, name='product-detail'),
    path('category/<str:slug>', views.categoryView, name='category'),
    path('s/', views.search, name='search'),
    path('wishlist/<int:pk>/', views.wishlist, name='wishlist')
]
