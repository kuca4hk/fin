from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturing_year = models.PositiveIntegerField()
    added_to_inventory = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.brand} - {self.model}'