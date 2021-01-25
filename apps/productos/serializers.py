from rest_framework import serializers
from apps.productos.models import Producto
#para que se liste todos los datos del proveedor lo exporto
from apps.proveedores.serializers import ProveedorSerializers
class ProductoSerializer(serializers.ModelSerializer):
    #para que se liste los datos del proveedor tambien
    proveedor = ProveedorSerializers(read_only = True)
    class Meta:
        model = Producto
        fields =('id','nombre','descripcion','precio','stock','proveedor')
class PostProductoSerializer(serializers.ModelSerializer):
    #para que se Guarde un nuevo
    class Meta:
        model = Producto
        fields =('id','nombre','descripcion','precio','stock','proveedor')
