# Generated by Django 2.2.3 on 2021-07-17 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_auto_20210716_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 23, 54, 55, 32278), verbose_name='Fecha de venta'),
        ),
    ]