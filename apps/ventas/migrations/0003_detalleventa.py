# Generated by Django 2.2.3 on 2020-12-20 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('ventas', '0002_auto_20201220_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Precio')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total a Pagar')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta', verbose_name='factura')),
            ],
            options={
                'verbose_name': 'Detalle de la Venta',
                'verbose_name_plural': 'Detalle de las Ventas',
            },
        ),
    ]
