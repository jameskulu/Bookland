from django.urls import path
from . import views

urlpatterns = [
    path('', views.used_books, name='used-books'),
    path('<int:pk>', views.used_books_detail, name='used-books-detail'),
    path('category/<str:slug>', views.used_categoryView,
         name='used-books-category'),
    path('s/', views.used_search, name='used-search'),
    path('listed-books/', views.listed_books, name='listed-books'),
    path('book-post/', views.book_post, name='book-post'),
    path('category-form/', views.category_form, name='category-form'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='update-book'),
    path('<int:pk>/delete/', views.delete_book, name='delete-book'),
]
