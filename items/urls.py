from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/item/<int:id>/', views.ItemsId.as_view()),
    path('api/items/<int:start>/<int:end>/', views.Items.as_view()),
    path('cart/item_add/<int:id>/', views.cart_add.as_view(), name='cart_add'),
    path('cart/item_clear/<int:id>/',
         views.item_clear.as_view(), name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment.as_view(), name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement.as_view(), name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear.as_view(), name='cart_clear'),
    path('cart/cart_items/', views.cart_items.as_view(), name='cart_clear'),
]
