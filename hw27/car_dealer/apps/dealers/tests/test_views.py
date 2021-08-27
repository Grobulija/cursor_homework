from django.test import TestCase

from apps.dealers.tests.factories import DealerFactory


class DealersListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = DealerFactory()
        cls.url = f'/dealers/'

    def test_pass(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class DealersDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dealer = DealerFactory()
        cls.url = f'/dealers/{cls.dealer.id}/'

    def test_pass(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dealer.title)

    def test_fail(self):
        response = self.client.get('/dealers/162452362/')
        self.assertEqual(response.status_code, 404)
