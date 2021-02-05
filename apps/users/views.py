from django.shortcuts import render
#api rest
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#serializers
from apps.users.serializers import UserLoginSerializer,UserModelSerializer,UserRegistrarseSerializer
#importar modelo
from apps.users.models import User
#si no encuentra el objeto
from django.shortcuts import get_object_or_404

class UserLoginAPIView(APIView):
    def post(self, request, *args, **Kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
          'user': UserModelSerializer(user).data,
          'access_token': token
        }
        return Response(data,status=status.HTTP_201_CREATED)
#metodos POst y Get
class UserGetPostAPIView(APIView):
    def get(self,request):
        usuarios = User.objects.all()
        usuarios_json = UserModelSerializer(usuarios, many=True)
        return Response(usuarios_json.data)

    def post(self, request, *args, **Kwargs):
        serializer = UserRegistrarseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data,status=status.HTTP_201_CREATED)

#metodos put delete,get individual
class UserGetPutDeleteView(APIView):
    #obtener el objeto de acuerdo al id que recibe
    def get_object (self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            usuario = get_object_or_404(User, pk=id)
    #mostrar un video de acuerdo a su id
    def get(self,request,id):
        usuario = self.get_object(id)
        usuario_json = UserModelSerializer(usuario)
        return Response(usuario_json.data)
    #actualizar registro de un usuario
    def put(self,request,id):
        usuario = self.get_object(id)
        usuario_json = UserModelSerializer(usuario, data=request.data)
        if usuario_json.is_valid():
            usuario_json.save() #guardar el usuario ya serializado
            return Response(usuario_json.data) # retorno los datos
        return Response(proveeedor_json.errors, status=400) #si no se pudo crear
    #eliminar usuario
    def delete(self,request,id):
        usuario = self.get_object(id)
        usuario.delete()
        return Response(status=204) # como ya se elimino no encontro ningun contenido
