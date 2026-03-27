from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    limite = models.IntegerField()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
