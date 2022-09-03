from django.urls import path, include
import accounts.views

urlpatterns = [
        path('login/',accounts.views.login),
        path('register/',accounts.views.register),
        path('index/',accounts.views.index),
] 
