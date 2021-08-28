from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Producent(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.producent}'


class PayMethod(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class Orders(models.Model):
    order_number = models.IntegerField(unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    if_delivery = models.BooleanField()
    date_delivery = models.DateTimeField(null=True, default='')
    payment_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)

    def __str__(self):
        return f'{self.order_number} {self.username} {self.if_delivery} {self.date_delivery} {self.payment_method} {self.product}'


class Opinions(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.username} {self.product} {self.date} {self.text}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='BasketProduct')


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)