from django.db import models
from ..cars.models import Car
from ..users.models import CustomUser
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class TransactionLog(models.Model):

    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted_car = models.JSONField(null=True, blank=True)
    deleted_car_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"{self.action} - {self.user}"

