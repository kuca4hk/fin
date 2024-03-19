from django.test import TestCase
from .models import Store, TransactionLog
from ..users.models import CustomUser
from ..cars.models import Car
from django.utils import timezone
import json
# Create your tests here.


class StoreModelTest(TestCase):

    def test_store_creation(self):
        store = Store.objects.create(name='Test Store', money=100000.00)
        self.assertIsInstance(store, Store)
        self.assertEqual(store.name, 'Test Store')
        self.assertEqual(store.money, 100000.00)

    def test_store_str_representation(self):
        store = Store.objects.create(name='Test Store', money=100000.00)
        self.assertEqual(str(store), 'Test Store')


class TransactionLogModelTest(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name='Test Store', money=100000.00)
        self.user = CustomUser.objects.create(email='test@example.com', password='testpassword')
        self.car = Car.objects.create(brand='Toyota', model='Corolla', price=25000.00, manufacturing_year=2023)

    def test_transaction_log_buy(self):
        transaction_log_buy = TransactionLog.objects.create(car=self.car, user=self.user, action='buy')
        self.assertIsInstance(transaction_log_buy, TransactionLog)
        self.assertEqual(transaction_log_buy.action, 'buy')
        self.assertEqual(transaction_log_buy.car, self.car)
        self.assertEqual(transaction_log_buy.user, self.user)
        self.assertTrue(timezone.now() - transaction_log_buy.timestamp < timezone.timedelta(seconds=1))


    def test_transaction_log_sell_creation(self):
        car_delete = {
            'brand': self.car.brand,
            'model': self.car.model,
            'price': self.car.price,
            'manufacturing_year': self.car.manufacturing_year
        }
        transaction_log_sell = TransactionLog.objects.create(user=self.user, action='sell', deleted_car=json.dumps(car_delete), deleted_car_price=self.car.price )
        self.assertIsInstance(transaction_log_sell, TransactionLog)
        self.assertEqual(transaction_log_sell.action, 'sell')
        self.assertEqual(transaction_log_sell.user, self.user)
        self.assertEqual(transaction_log_sell. deleted_car, json.dumps(car_delete))
        self.assertEqual(transaction_log_sell.deleted_car_price, self.car.price)
        self.assertTrue(timezone.now() - transaction_log_sell.timestamp < timezone.timedelta(seconds=1))