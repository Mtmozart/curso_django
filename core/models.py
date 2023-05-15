from django.db import models

# Create your models here - comando para execultar a migration python menage.py makemigration e migrate para execultar.

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantidade em estoque')

class Client(models.Model):
    name = models.CharField('Nome', max_length=20)
    last_name = models.CharField('Sobrenome', max_length=20)
    email = models.EmailField('E-mail', max_length=100)

