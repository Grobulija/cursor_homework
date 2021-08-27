from django.test import TestCase

from apps.orders.tests.factories import OrderFactory


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = OrderFactory()
        cls.url = f'/orders/'

    def test_pass(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class DealersDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.order = OrderFactory()
        cls.url = f'/orders/{cls.order.id}/'

    def test_pass(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.email)

    def test_fail(self):
        response = self.client.get('/dealers/4536123/')
        self.assertEqual(response.status_code, 404)
