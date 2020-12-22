from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#para usar la APIView de la libreria rest_framework
from rest_framework.views import APIView
#para retornar json
from rest_framework.response import Response
# importo la clase serializadora
from apps.proveedores.serializers import ProveedorSerializers
# importo mi modelo
from apps.proveedores.models import Proveedor
class ListarProveedores(APIView):
    def get(self, request):
        proveedores = Proveedor.objects.all()
        proveedor_json = ProveedorSerializers(proveedores, many=True)
        return Response(proveedor_json.data)
