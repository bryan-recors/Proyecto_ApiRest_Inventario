from django.shortcuts import render
from rest_framework.views import APIView
from apps.productos.models import Producto
from rest_framework.response import Response
from apps.productos.serializers import ProductoSerializer
# Create your views here.
class ListarProductos(APIView):
    def get(self,request):
        productos = Producto.objects.all()
        producto_json = ProductoSerializer(productos, many=True)
        return Response(producto_json.data)
