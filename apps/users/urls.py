from django.urls import path
from apps.users.views import UserLoginAPIView,UserGetPostAPIView,UserGetPutDeleteView,UserSearchListView

urlpatterns = [
    path('usuario/login/',UserLoginAPIView.as_view(),name='login'),
    path('usuarios/',UserGetPostAPIView.as_view(),name='usuarios'),
    path('usuarios/<int:id>',UserGetPutDeleteView.as_view(),name='detalle_usuarios'),
    path('usuarios/search',UserSearchListView.as_view(),name='search'),
]
