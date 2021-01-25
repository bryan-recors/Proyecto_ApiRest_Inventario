from django.db import models
from apps.proveedores.models import Proveedor

from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField('Nombre del Producto',max_length=50, unique=True)
    descripcion = models.TextField('Descripcion',blank=True, null=True)
    precio = models.FloatField('Precio de venta')
    stock=models.IntegerField('Cantidad existente')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,verbose_name="Proveedor")
    def clean(self):
        if self.nombre.isdigit():
            raise ValidationError('El campo "Nombre" no puede ser numerico')
        else:
            if self.stock < 0:
                raise ValidationError('El campo "Cantidad Existente" no pueden ser un numero negativo')
            else:
                if self.stock ==0:
                    raise ValidationError('El campo "Cantidad Existente" debe ser mayor a 1 unidad')
    
    # para conocer cuantos productos se Registro
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
