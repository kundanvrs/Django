from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('faculty/',views.faculty,name='faculty'),
]
