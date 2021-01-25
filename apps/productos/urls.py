from django.urls import path
from apps.productos.views import ListarProductos,DetalleProducto,ProductosSearchListView
urlpatterns = [
    path('productos/',ListarProductos.as_view(),name='productos'),
    path('productos/<int:id>',DetalleProducto.as_view(),name='detalle_producto'),
    path('productos/search',ProductosSearchListView.as_view(),name='search'),
]
