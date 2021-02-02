from django.db import models
from apps.productos.models import Producto
from datetime import datetime
# Create your models here.
class Venta(models.Model):
    fecha = models.DateField('Fecha de venta',default=datetime.now)
    subtotal = models.DecimalField('Subtotal',default=0.00,max_digits=9,decimal_places=2)
    iva = models.DecimalField('Iva',default=0.00,max_digits=9,decimal_places=2)
    total= models.DecimalField('Total a Pagar',default=0.00,max_digits=9,decimal_places=2)
    class Meta:
        verbose_name= 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha']
 
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE,verbose_name="factura")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,verbose_name="Producto")
    precio = models.DecimalField('Precio',default=0.00,max_digits=9,decimal_places=2)
    cantidad = models.IntegerField('Cantidad',default=0)
    subtotal= models.DecimalField('Total a Pagar',default=0.00,max_digits=9,decimal_places=2)
    class Meta:
        verbose_name= 'Detalle de la Venta'
        verbose_name_plural = 'Detalle de las Ventas'
