from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('subscribe/', views.email_list_signup, name='subscribe'),
]
