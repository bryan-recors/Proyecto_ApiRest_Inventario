from django.urls import path
from apps.ventas.views import Ventas
urlpatterns = [
    path('ventas/',Ventas.as_view(),name='ventas'),
    #path('productos/<int:id>',DetalleProducto.as_view(),name='detalle_producto'),
]
