from django.contrib import admin
from django.urls import path
from diabetes_app.views import index
urlpatterns = [
    path('', index),
]