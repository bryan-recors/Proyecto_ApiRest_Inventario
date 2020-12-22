from django.urls import path
from apps.proveedores.views import ListarProveedores

urlpatterns = [
    path('listar_proveedores/',ListarProveedores.as_view(),name='listar_proveedores'),
]
