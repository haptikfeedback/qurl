from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404

from . import views

urlpatterns = [
    path('shorten', views.shorten, name='shorten'),
    path('', views.index, name='index'),
    path('<str:code>', views.redirect)
]