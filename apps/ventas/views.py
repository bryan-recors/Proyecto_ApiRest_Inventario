from django.shortcuts import render
from rest_framework.views import APIView
from apps.ventas.models import Venta
from rest_framework.response import Response
from apps.ventas.serializers import VentaSerializer
#para cuando no existe un ventas
from django.shortcuts import get_object_or_404
# Listar la lista de ventas
class Ventas(APIView):
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
