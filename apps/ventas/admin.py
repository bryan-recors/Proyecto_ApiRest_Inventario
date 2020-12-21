from django.contrib import admin
from apps.ventas.models import Venta,DetalleVenta
# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    list_display = ('__str__','fecha','subtotal','iva','total')
    #filtro
    list_filter=('subtotal','total')

admin.site.register(Venta,VentaAdmin)

class DetalleVentaAdmin(admin.ModelAdmin):
    #lo que se va a mostrar al listar
    list_display = ('__str__','venta','producto','precio','cantidad','subtotal')
    #filtro
    list_filter=('cantidad','subtotal')

admin.site.register(DetalleVenta,DetalleVentaAdmin)
