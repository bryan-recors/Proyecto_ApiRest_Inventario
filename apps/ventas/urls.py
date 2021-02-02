from django.urls import path
from apps.ventas.views import VentasView,DetalleVentaView
urlpatterns = [
    path('ventas/',VentasView.as_view(),name='ventas'),
    path('detalle_ventas/',DetalleVentaView.as_view(),name='detalle_ventas'),
]
