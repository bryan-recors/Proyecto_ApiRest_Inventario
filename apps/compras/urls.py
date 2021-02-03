from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.compras.views import CompraViewSet,DetalleCompraViewSet
#compra
router = DefaultRouter()
router.register(r'compras',CompraViewSet,basename='compras')
#detalleCompra
router2 = DefaultRouter()
router2.register(r'detalle_compras',DetalleCompraViewSet,basename='detalle_compras')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router2.urls))
]
