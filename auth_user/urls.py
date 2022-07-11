from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('user_details/', views.user_details.as_view()),
    path('activate/<uidb64>/<token>', views.activate.as_view(), name='activate'),
    path('forgotPassword/', views.forgotPassword.as_view(), name='forgotPassword'),
    path('resetPassword/<uidb64>/<token>',
         views.resetPassword.as_view(), name='resetPassword'),
    path("OAuth/<provider>/", views.OAuth.as_view(), name="google"),
]
