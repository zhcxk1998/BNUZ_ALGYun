from django.contrib import admin
from django.urls import path
from .views import register, login
app_name = 'account'
urlpatterns = [
    path('register/', register, name='my_register'),
    path('login/', login, name='my_login'),
]