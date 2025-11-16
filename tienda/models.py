from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# -------------------------------
# MODELO DE PRODUCTO
# -------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=100)  # nombre del archivo en /static/imagenes/
    categoria = models.CharField(max_length=50, default='general')  # ejemplo: 'collares', 'anillos'

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

# -------------------------------
# MODELO DE ITEM EN EL CARRITO
# -------------------------------
class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

    class Meta:
        verbose_name = "Item de Carrito"
        verbose_name_plural = "Items de Carrito"

# -------------------------------
# MODELO DE PEDIDO CONFIRMADO
# -------------------------------
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

# -------------------------------
# MODELO DE ITEM EN EL PEDIDO
# -------------------------------
class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Items de Pedido"

