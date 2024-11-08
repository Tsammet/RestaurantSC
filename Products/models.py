from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)

    # ESTE ES UN METODO PARA DEFINIR COMO SE MUESTRA EL OBJETO AL IMPRIMIRLO
    def __str__(self):
        return self.name