# Generated by Django 3.0.8 on 2020-08-02 15:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.FloatField(default=0)),
                ('iva', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date(2020, 8, 2))),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['cliente'],
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('subtotal', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto')),
            ],
            options={
                'verbose_name': 'DetalleFactura',
                'verbose_name_plural': 'DetalleFacturas',
                'ordering': ['factura'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ManyToManyField(to='app.Producto'),
        ),
    ]