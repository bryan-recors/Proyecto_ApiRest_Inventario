# Generated by Django 2.2.3 on 2021-07-17 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_auto_20210215_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 23, 15, 57, 859052), verbose_name='Fecha de venta'),
        ),
    ]
