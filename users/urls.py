from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')), #URLs that handle user accounts are part of django framwork, we don't have to create them
    path('register/', views.register,name='register'),
]