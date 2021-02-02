from django.urls import path
from apps.users.views import UserLoginAPIView,UserRegistrarseAPIView

urlpatterns = [
    path('users/login/',UserLoginAPIView.as_view(),name='login'),
    path('users/registrarse/',UserRegistrarseAPIView.as_view(),name='registrarse'),
]
