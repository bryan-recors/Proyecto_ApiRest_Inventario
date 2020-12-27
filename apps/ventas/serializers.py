from rest_framework import serializers
from apps.ventas.models import Venta,DetalleVenta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =('id','fecha','subtotal','iva','total')

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields =('id','venta','producto','precio','cantidad','subtotal')
