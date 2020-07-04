from django.urls import path
from . import views


urlpatterns = [
    path('manage-profile', views.profile, name="manage-profile"),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('change-password', views.change_password, name="change-password")
]
