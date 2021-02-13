from django.shortcuts import render
from rest_framework import viewsets
from apps.compras.models import Compra,DetalleCompra
from apps.compras.serializers import CompraModelSerializer,DetalleCompraModelSerializer
# Create your views here.
#para usar la APIView de la libreria rest_framework
from rest_framework.views import APIView
#para retornar json
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraModelSerializer

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraModelSerializer

class FullDetalleCompraViewSet(APIView):
    def get(self, request, id):
        detalles = DetalleCompra.objects.filter(compra__id = id)
        detalleCompra_json = DetalleCompraModelSerializer(detalles, many=True)
        return Response(detalleCompra_json.data)
        #Crear registro de Proveedores
