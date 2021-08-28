from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/', views.SignUp.as_view(), name='signup'),
]