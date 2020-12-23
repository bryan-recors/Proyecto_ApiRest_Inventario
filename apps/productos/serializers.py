from rest_framework import serializers
from apps.productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =('id','nombre','descripcion','precio','stock','proveedor')
