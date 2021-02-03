from django.contrib import admin
from apps.compras.models import Compra,DetalleCompra
# Register your models here.

class CompraAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','proveedor','total')
    #filtro
    list_filter=('fecha','total')

admin.site.register(Compra,CompraAdmin)

class DetalleCompraAdmin(admin.ModelAdmin):
    #lo que se va a mostrar al listar
    list_display = ('id','venta','producto','precio_compra','cantidad','subtotal')
    #filtro
    list_filter=('cantidad','subtotal')

admin.site.register(DetalleCompra,DetalleCompraAdmin)
