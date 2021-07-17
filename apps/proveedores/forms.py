from django import forms
from .models import Proveedor

class FormularioProveedor(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Proveedor
        fields = ('nombre','descripcion','telefono','celular','email','dias_visita','imagen')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre del Proveedor',
            'descripcion':'Descripción',
            'telefono':'Telefono',
            'celular': 'Celular',
            'email':'Email',
            'dias_visita': "Dias de visita",
            'imagen': 'Imagen'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del proveedor',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el telefono',
                }
            ),
            'celular': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'celular',
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'email',
                }
            ),
            'dias_visita': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'dias de visita',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            )
        }
