from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
]
