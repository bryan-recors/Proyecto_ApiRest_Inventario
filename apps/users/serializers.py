from apps.users.models import User
#rest rest_framework
from rest_framework import serializers
#django para autenticar
from django.contrib.auth import authenticate
#Token
from rest_framework.authtoken.models import Token
#unique Validation
from rest_framework.validators import UniqueValidator
#para usar regex validator
from django.core.validators import RegexValidator
#para validar q coincidan contraseñas
from django.contrib.auth import password_validation


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

#para validad y crear registro se hereda serializer.serializer
class UserRegistrarseSerializer(serializers.Serializer):
    #validacion y creacion de usuario
    email=serializers.EmailField(
        validators= [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length = 4,
        max_length = 20,
        validators= [UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(min_length=2, max_length=100)
    last_name = serializers.CharField(min_length=2, max_length=100)
    celular_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="el formato de numero de ser: +9999999999"
    )
    celular= serializers.CharField(validators=[celular_regex])
    vendedor =serializers.BooleanField(default=False)
    #validacion del numero de celular
    password = serializers.CharField(min_length=8, max_length=64)
    confirmacion_password = serializers.CharField(min_length=8, max_length=64)
    def validate(self,data):
        #verificar contraseña
        passwd = data['password']
        passwd_conf = data['confirmacion_password']
        if passwd != passwd_conf:
            raise serializer.ValidationError("contraselas no coinciden")
        password_validation.validate_password(passwd)
        return data

    def create(self,data):
        #crear usuario
        #sacar la confirmacion del password
        data.pop('confirmacion_password')
        user= User.objects.create_user(**data)
        return user
