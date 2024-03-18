from django.test import TestCase
from .models import Store, TransactionLogBuy, TransactionLogSell
from ..users.models import CustomUser
from ..cars.models import Car
from django.utils import timezone
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


class TransactionLogBuyModelTest(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name='Test Store', money=100000.00)
        self.user = CustomUser.objects.create(email='test@example.com', password='testpassword')
        self.car = Car.objects.create(brand='Toyota', model='Corolla', price=25000.00, manufacturing_year=2023)

    def test_transaction_log_buy_creation(self):
        transaction_log_buy = TransactionLogBuy.objects.create(car=self.car, user=self.user)
        self.assertIsInstance(transaction_log_buy, TransactionLogBuy)
        self.assertEqual(transaction_log_buy.action, 'buy')
        self.assertEqual(transaction_log_buy.car, self.car)
        self.assertEqual(transaction_log_buy.user, self.user)
        self.assertTrue(timezone.now() - transaction_log_buy.timestamp < timezone.timedelta(seconds=1))

    def test_transaction_log_buy_action_change(self):
        transaction_log_buy = TransactionLogBuy.objects.create(car=self.car, user=self.user)
        transaction_log_buy.action = 'sell'
        with self.assertRaises(ValueError):
            transaction_log_buy.save()


class TransactionLogSellModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='test@example.com', password='testpassword')

    def test_transaction_log_sell_creation(self):
        transaction_log_sell = TransactionLogSell.objects.create(car_model='Corolla', car_brand='Toyota', car_price=25000.00, user=self.user)
        self.assertIsInstance(transaction_log_sell, TransactionLogSell)
        self.assertEqual(transaction_log_sell.action, 'sell')
        self.assertEqual(transaction_log_sell.car_model, 'Corolla')
        self.assertEqual(transaction_log_sell.car_brand, 'Toyota')
        self.assertEqual(transaction_log_sell.car_price, 25000.00)
        self.assertEqual(transaction_log_sell.user, self.user)
        self.assertTrue(timezone.now() - transaction_log_sell.timestamp < timezone.timedelta(seconds=1))

    def test_transaction_log_sell_action_change(self):
        transaction_log_sell = TransactionLogSell.objects.create(car_model='Corolla', car_brand='Toyota', car_price=25000.00, user=self.user)
        transaction_log_sell.action = 'buy'
        with self.assertRaises(ValueError):
            transaction_log_sell.save()
