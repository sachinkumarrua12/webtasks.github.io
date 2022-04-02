from unicodedata import name
from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('sign_up',views.sign_up ,name='sign_up'),
    path('user_login',views.user_login ,name='user_login'),
    path('profile',views.profile, name= 'profile'),
    path('user_logout',views.user_logout, name= 'user_logout'),
]