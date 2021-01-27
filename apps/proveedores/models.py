from django.db import models
# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField('Nombre del Proveedor',max_length=50)
    descripcion = models.TextField('Descripcion',blank=True, null=True,)
    telefono = models.CharField('Teléfono',max_length=10)
    celular = models.CharField('Celular',max_length=10,blank=True, null=True)
    email = models.EmailField('Correo',blank=True, null=True)
    dias_visita = models.CharField('Dias de visita',max_length=300)
    # para conocer cuanto una parroquias se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
