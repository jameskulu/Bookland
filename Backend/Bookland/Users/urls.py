from django.urls import path
from . import views


urlpatterns = [
    path('manage-profile', views.profile, name="manage-profile"),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('change-password', views.change_password, name="change-password"),
    path('favrioute-list/', views.favrioute_list, name="favrioute-list"),
    path('orders/', views.my_orders, name="orders"),
    path('<int:pk>/cancel-book/', views.cancel_book, name='cancel-book'),
]
