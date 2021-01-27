from apps.users.models import User
#rest rest_framework
from rest_framework import serializers
#django para autenticar
from django.contrib.auth import authenticate
#Token
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        #validar credenciales
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales invalidas')
        self.context['user'] = user
        return data
    #manejar el Token
    def create(self, data):
       #generar un new token
       token, created = Token.objects.get_or_create(user=self.context['user'])
       return self.context['user'],token.key

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','first_name','last_name','email','celular')
