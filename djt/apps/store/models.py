from django.db import models
from ..cars.models import Car
from ..users.models import CustomUser
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class TransactionLogBuy(models.Model):
    BUY = 'buy'

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, default=BUY)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.action = self.BUY
        else:
            if self.action != self.BUY:
                raise ValueError("Hodnota pole nesmí být změněna.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.action} - {self.car}'


class TransactionLogSell(models.Model):
    SELL = 'sell'

    car_model = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, default=SELL)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.action = self.SELL
        else:
            if self.action != self.SELL:
                raise ValueError("Hodnota pole nesmí být změněna.")
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.action} - {self.car_model}'


