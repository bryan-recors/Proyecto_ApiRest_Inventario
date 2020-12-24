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
from django.shortcuts import get_object_or_404
class ListarProveedores(APIView):
    def get(self, request):
        proveedores = Proveedor.objects.all()
        proveedor_json = ProveedorSerializers(proveedores, many=True)
        return Response(proveedor_json.data)
        #Crear registro de Proveedores
        def post(self, request):
            proveedor_json=ProveedorSerializers(data=request)
            if proveedor_json.isvalid():
                proveedor_json.save()
                return Response(proveedor_json.data, status=201)
            return Response(proveedor_json.erros, status=400)
#listar un proveedor
class DetalleProveedor(APIView):
    #obtener el objeto de acuerdo al id que recibe
    def get_object (self,id):
        try:
            return Proveedor.objects.get(id=id)
        except Proveedor.DoesNotExist:
            proveedor = get_object_or_404(Proveedor, pk=id)
    #mostrar un video de acuerdo a su id
    def get(self,request,id):
        proveedor = self.get_object(id)
        proveedor_json = ProveedorSerializers(proveedor)
        return Response(proveedor_json.data)
    #actualizar registro de un proveedor
    def put(self,request,id):
        proveedor = self.get_object(id)
        proveedor_json = ProveedorSerializers(proveedor, data=request.data)
        if proveedor_json.is_valid():
            proveedor_json.save() #guardar el proveedor ya serializado
            return Response(proveedor_json.data) # retorno los datos
        return Response(proveeedor_json.errors, status=400) #si no se pudo crear
    #eliminar proveedor
    def delete(self,request,id):
        proveedor = self.get_object(id)
        proveedor.delete()
        return Response(status=204) # como ya se elimino no encontro ningun contenido
