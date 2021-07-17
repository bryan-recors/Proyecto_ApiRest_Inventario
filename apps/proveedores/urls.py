from django.urls import path
from apps.proveedores.views import ListarProveedores, DetalleProveedor,ProveedorSearchListView,RegistrarProveedor
#crear formulario

urlpatterns = [
    path('registrar_proveedor/',RegistrarProveedor.as_view(),name ='registrar_proveedor'),
    path('proveedores/',ListarProveedores.as_view(),name='proveedores'),
    path('proveedores/<int:id>',DetalleProveedor.as_view(),name='detalle_proveedores'),
    path('proveedores/search',ProveedorSearchListView.as_view(),name='search'),
]
