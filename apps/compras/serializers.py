
from rest_framework import serializers
from apps.compras.models import Compra,DetalleCompra

class CompraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields =('id','fecha','proveedor','total')

class DetalleCompraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields =('id','compra','producto','precio_compra','cantidad','subtotal')
