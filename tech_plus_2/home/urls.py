from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name='register'),
    path('signup/home/', views.SignUp, name='home'),
    path('signin/dashboard/', views.SignIn, name='home'),
    path('signin/', views.SignInPage, name='signInPage'),
    path('signup/', views.SignUpPage, name='signUpPage'),
    path('terms/', views.TermsPage, name='TermsPage'),
    path('policy/', views.PolicyPage, name='PolicyPage'),
    path('pricing/', views.PricingPage, name='pricing'),
    #path('policy/', views.emPage, name='PolicyPage'),
]