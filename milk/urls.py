from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sample/', views.sample.as_view(), name='login'),
]
