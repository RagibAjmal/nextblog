from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/<int:id>', views.Items.as_view()),
]
