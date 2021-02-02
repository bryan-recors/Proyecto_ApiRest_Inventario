# Create mi propio user
from django.db import models
from django.contrib.auth.models import AbstractUser
#utilidades

class User(AbstractUser):
    email = models.EmailField('correo', unique=True, error_messages={'unique': 'ya existe un usuario con este correp'})
    first_name = models.CharField('Nombres',max_length=100)
    last_name = models.CharField('Apellidos',max_length=100)
    celular = models.CharField('Celular',max_length=15, blank=True, null=True)
    vendedor = models.BooleanField('Es vendedor', default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']
    def __str__(self):
        return self.username
    def get_short_name(self):
        #return username
        return self.username
