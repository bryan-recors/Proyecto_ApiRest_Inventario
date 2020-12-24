from django.urls import path
from apps.proveedores.views import ListarProveedores, DetalleProveedor

urlpatterns = [
    path('proveedores/',ListarProveedores.as_view(),name='proveedores'),
    path('proveedores/<int:id>',DetalleProveedor.as_view(),name='detalle_proveedores'),
]
