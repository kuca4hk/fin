from django.db import models
from ..cars.models import Car
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class TransactionLog(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # buy or sell
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} - {self.car}'