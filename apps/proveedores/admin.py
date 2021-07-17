from django.contrib import admin
from apps.proveedores.models import Proveedor
# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    # que campos aparecen en el formulario si no lo pongo apareceran todos los del model
    #fields = ('nombre','descripcion','telefono','celular','email','dias_visita')
    #lo que se va a mostrar al listar
    list_display = ('nombre','telefono','celular','email','dias_visita','imagen','created_at')
    #buscador por nombre y dias de visita
    search_fields = ('nombre','dias_visita')
    #filtro
    list_filter=('nombre','dias_visita','email')

admin.site.register(Proveedor,ProveedorAdmin)
