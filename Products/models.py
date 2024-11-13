from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'categories/', blank= True, null=True)

    # ESTE ES UN METODO PARA DEFINIR COMO SE MUESTRA EL OBJETO AL IMPRIMIRLO
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name