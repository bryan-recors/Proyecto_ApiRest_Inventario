from django.shortcuts import render
from rest_framework import viewsets
from apps.compras.models import Compra,DetalleCompra
from apps.compras.serializers import CompraModelSerializer,DetalleCompraModelSerializer
# Create your views here.

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraModelSerializer

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraModelSerializer
