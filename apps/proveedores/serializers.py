from rest_framework import serializers
from apps.proveedores.models import Proveedor

class ProveedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        # indicarle que campos vamos a serializar se envia una tupla
        fields = ('id','nombre','descripcion','telefono','celular','email','dias_visita','imagen')
