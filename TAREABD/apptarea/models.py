from django.db import models


class Producto(models.Model):
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return self.descripcion




