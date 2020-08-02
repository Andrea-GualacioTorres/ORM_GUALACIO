from django.db import models
from datetime import date

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural = 'Productos'
        ordering=['descripcion']

    def __str__(self):
        return '{}'.format(self.descripcion)


class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural = 'Clientes'
        ordering=['nombre']

    def __str__(self):
        return '{}'.format(self.nombre)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField(default= date.today())
    total = models.FloatField(default=0)

    class Meta:
        verbose_name='Factura'
        verbose_name_plural = 'Facturas'
        ordering=['cliente']

    def __str__(self):
        return '{}'.format(self.cliente)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    class Meta:
        verbose_name='DetalleFactura'
        verbose_name_plural = 'DetalleFacturas'
        ordering=['factura']
    def __str__(self):
        return '{}'.format(self.factura)
