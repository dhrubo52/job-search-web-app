from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path('obtain_token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify_token/', TokenVerifyView.as_view(), name='verify_token'),
    path('register/', views.Register.as_view(), name='register'),
]