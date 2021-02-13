#**********una forma efectiva de hacerlo para las viewsets****
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ventas.views import VentaViewSet,DetalleVentaViewSet,FullDetalleVentaViewSet
#compra
router = DefaultRouter()
router.register(r'ventas',VentaViewSet,basename='ventas')
#detalleCompra
router2 = DefaultRouter()
router2.register(r'detalle_ventas',DetalleVentaViewSet,basename='detalle_ventas')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router2.urls)),
    #path('detalle_ventas_porventa/<pk>',FullDetalleVentaViewSet.as_view(), name ='detalle_ventas_porventa'),
    path('detalle_ventas_porventa/<int:id>',FullDetalleVentaViewSet.as_view(),name='detalle_ventas_porventa'),
]

#********la forma clasica de hacerlo **************
"""
from django.urls import path
from apps.ventas.views import VentasView,DetalleVentaView
urlpatterns = [
    path('ventas/',VentasView.as_view(),name='ventas'),
    path('detalle_ventas/',DetalleVentaView.as_view(),name='detalle_ventas'),
]
"""
