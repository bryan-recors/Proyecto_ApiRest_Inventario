from django.urls import path
from apps.productos.views import ListarProductos
urlpatterns = [
    path('listar_producto/',ListarProductos.as_view(),name='listar_producto'),
]
