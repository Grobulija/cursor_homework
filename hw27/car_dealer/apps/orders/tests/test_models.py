from django.test import TestCase

from apps.cars.tests.factories import CarFactory
from apps.orders.models import Order


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Kateryna',
            last_name='Supruniuk',
            email='kate@gmail.com',
            phone='+1563456535',
            message='test message',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Kateryna Supruniuk')
        self.assertEqual(order.email, 'kate@gmail.com')
        self.assertEqual(order.phone, '+1563456535')
        self.assertEqual(order.message, 'test message')
