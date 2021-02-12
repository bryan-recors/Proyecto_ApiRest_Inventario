from django.urls import path
from apps.proveedores.views import ListarProveedores, DetalleProveedor,ProveedorSearchListView

urlpatterns = [
    path('proveedores/',ListarProveedores.as_view(),name='proveedores'),
    path('proveedores/<int:id>',DetalleProveedor.as_view(),name='detalle_proveedores'),
    path('proveedores/search',ProveedorSearchListView.as_view(),name='search'),
]
