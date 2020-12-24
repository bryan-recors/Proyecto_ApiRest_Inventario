from django.db import models
from apps.proveedores.models import Proveedor
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField('Nombre del Producto',max_length=50, unique=True)
    descripcion = models.TextField('Descripcion',blank=True, null=True)
    precio = models.FloatField('Precio de venta')
    stock=models.IntegerField('Cantidad existentess')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,verbose_name="Proveedor")
    # para conocer cuanto una parroquias se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
