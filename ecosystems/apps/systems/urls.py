from django.contrib import admin
from django.urls import path
from ecosystems.apps.systems import views

urlpatterns = [
    path('', views.log_in),
]
