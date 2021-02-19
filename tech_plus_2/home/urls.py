from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name='register'),
    path('signup/home/', views.SignUp, name='home'),
    path('signin/dashboard/', views.SignIn, name='home'),
    path('signin/', views.SignInPage, name='signInPage'),
    path('signup/', views.SignUpPage, name='signInPage'),
]