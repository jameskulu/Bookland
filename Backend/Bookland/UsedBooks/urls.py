from django.urls import path
from . import views

urlpatterns = [
    path('', views.used_books, name='used-books'),
    path('<int:pk>', views.used_books_detail, name='used-books-detail'),
    path('category/<str:slug>', views.used_categoryView,
         name='used-books-category'),
    path('s/', views.used_search, name='used-search'),
    path('listed-books/', views.listed_books, name='listed-books'),
]
