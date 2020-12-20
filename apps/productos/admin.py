from django.contrib import admin
from apps.productos.models import Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    #lo que se va a mostrar al listar
    list_display = ('nombre','precio','stock','proveedor','created_at')
    #buscador por nombre y stock
    search_fields = ('nombre','stock')
    #filtro
    list_filter=('nombre','precio','stock')

admin.site.register(Producto,ProductoAdmin)
