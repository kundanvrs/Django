from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('home/',views.HomePage,name='homepage'),
    path('login/',views.handleLogin,name='handlelogin'),
    path('logout/',views.handleLogout,name='handlelogout'),
    path('signup/',views.handleSignup,name='handlesignup'),

    
]
