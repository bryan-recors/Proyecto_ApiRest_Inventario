#********** una mejor forma de hacerlo con viewsets sin tener q poner todos los metodos*
from django.shortcuts import render
from rest_framework import viewsets
from apps.ventas.models import Venta,DetalleVenta
from apps.ventas.serializers import VentaSerializer,DetalleVentaSerializer
# Create your views here.

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer

#¨*********************una forma mas larga de hacerlo********************
"""
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from apps.ventas.serializers import VentaSerializer,DetalleVentaSerializer
#para cuando no existe un ventas
from django.shortcuts import get_object_or_404
# Listar la lista de ventas
class VentasView(APIView):
    #listar un registro
    def get(self,request):
        ventas = Venta.objects.all()
        venta_json = VentaSerializer(ventas, many=True)
        return Response(venta_json.data)
    #crear un registro
    def post(self,request):
        venta_json = VentaSerializer(data=request.data) #UnMarshall
        if venta_json.is_valid():
            venta_json.save()
            return Response(venta_json.data, status=201) # si se creo
        return Response(venta_json.errors, status=400) #si no se pudo crear

class DetalleVentaView(APIView):
    #listar un registro
    def get(self,request):
        detalle = DetalleVenta.objects.all()
        detalle_json = DetalleVentaSerializer(detalle, many=True)
        return Response(detalle_json.data)
    #crear un registro
    def post(self,request):
        detalle_json = DetalleVentaSerializer(data=request.data) #UnMarshall
        if detalle_json.is_valid():
            detalle_json.save()
            return Response(detalle_json.data, status=201) # si se creo
        return Response(detalle_json.errors, status=400) #si no se pudo crear
"""
