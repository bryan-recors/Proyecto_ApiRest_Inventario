from django.db import models
from apps.productos.models import Producto
from apps.proveedores.models import Proveedor
from datetime import datetime
# Create your models here.
class Compra(models.Model):
    fecha = models.DateField('Fecha de compra',default=datetime.now)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,verbose_name="Proveedor")
    total= models.DecimalField('Total pagado',default=0.00,max_digits=9,decimal_places=2)
    class Meta:
        verbose_name= 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['fecha']

class DetalleCompra(models.Model):
    venta = models.ForeignKey(Compra, on_delete=models.CASCADE,verbose_name="Compra")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,verbose_name="Producto")
    precio_compra = models.DecimalField('Precio_compra',default=0.00,max_digits=9,decimal_places=2)
    cantidad = models.IntegerField('Cantidad',default=0)
    subtotal= models.DecimalField('Total a Pagar',default=0.00,max_digits=9,decimal_places=2)
    class Meta:
        verbose_name= 'Detalle de la compra'
