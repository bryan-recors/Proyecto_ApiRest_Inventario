from django.shortcuts import render
from rest_framework.views import APIView
from apps.productos.models import Producto
from rest_framework.response import Response
from apps.productos.serializers import ProductoSerializer,PostProductoSerializer
#para cuando no existe un productos
from django.shortcuts import get_object_or_404
# Listar la lista de productos
class ListarProductos(APIView):
    #listar un registro
    def get(self,request):
        productos = Producto.objects.all()
        producto_json = ProductoSerializer(productos, many=True)
        return Response(producto_json.data)
    #crear un registro
    def post(self,request):
        producto_json = PostProductoSerializer(data=request.data) #UnMarshall
        if producto_json.is_valid():
            producto_json.save()
            return Response(producto_json.data, status=201) # si se creo
        return Response(producto_json.errors, status=400) #si no se pudo crear

#listar un producto en concreto
class DetalleProducto(APIView):
    #obtener el objeto de acuerdo al id que recibe
    def get_object (self,id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            producto = get_object_or_404(Producto, pk=id)
    #mostrar un video de acuerdo a su id
    def get(self,request,id):
        producto = self.get_object(id)
        producto_json = PostProductoSerializer(producto)
        return Response(producto_json.data)
    #actualizar registro de un producto
    def put(self,request,id):
        producto = self.get_object(id)
        producto_json = PostProductoSerializer(producto, data=request.data)
        if producto_json.is_valid():
            producto_json.save() #guardar el producto ya serializado
            return Response(producto_json.data) # retorno los datos
        return Response(producto_json.errors, status=400) #si no se pudo crear
    #eliminar producto
    def delete(self,request,id):
        producto = self.get_object(id)
        producto.delete()
        return Response(status=204) # como ya se elimino no encontro ningun contenido

#buscar un producto por su nombre
class ProductosSearchListView(APIView):
    def get_queryset(self):
        try:
            return Producto.objects.filter(nombre__icontains=self.query())
        except Producto.DoesNotExist:
            producto = get_object_or_404(Producto, nombre=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get(self,request):
        productos = self.get_queryset()
        producto_json = ProductoSerializer(productos, many=True)
        return Response(producto_json.data)
