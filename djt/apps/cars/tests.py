from django.test import TestCase
from django.utils import timezone
from .models import Car


class CarModelTest(TestCase):

    def test_car_creation(self):
        car = Car.objects.create(
            brand='Ferrari',
            model='f1',
            price=25000.00,
            manufacturing_year=2023
        )
        self.assertIsInstance(car, Car)
        self.assertEqual(car.brand, 'Ferrari')
        self.assertEqual(car.model, 'f1')
        self.assertEqual(car.price, 25000.00)
        self.assertEqual(car.manufacturing_year, 2023)
        self.assertTrue(car.added_to_inventory <= timezone.now())

    def test_car_str_representation(self):
        car = Car.objects.create(
            brand='RedBull',
            model='RB16',
            price=25000.00,
            manufacturing_year=2021
        )
        self.assertEqual(str(car), 'RedBull - RB16')