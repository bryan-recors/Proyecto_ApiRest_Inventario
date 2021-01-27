from django.urls import path
from apps.users.views import UserLoginAPIView

urlpatterns = [
    path('users/login/',UserLoginAPIView.as_view(),name='login'),
]
