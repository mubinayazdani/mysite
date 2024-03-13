from django.urls import path 

from .views import RegisterView, GetTOkenView 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    
    path('register/', RegisterView.as_view()),
    path('get-token/', GetTOkenView.as_view()),
    
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh', TokenRefreshView.as_view())
]
