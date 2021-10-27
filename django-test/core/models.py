from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.DecimalField('price', decimal_places=2, max_digits=9)
    storage = models.IntegerField('storage')

    def __str__(self):
        return self.name



class Client(models.Model):
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email', max_length=50)

    def __str__(self):
        return self.name