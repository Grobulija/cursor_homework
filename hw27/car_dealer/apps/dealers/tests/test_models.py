from django.test import TestCase

from apps.dealers.tests.factories import UserFactory, CityFactory, CountryFactory
from apps.dealers.models import Dealer, City, Country


class TestDealerModel(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.city = CityFactory()

    def test_model(self):
        dealer = Dealer.objects.create(
            title='dealer',
            e_mail='dealer@gmail.com',
            user=self.user,
            city=self.city,
        )

        self.assertIsNotNone(dealer.id)
        self.assertEqual(str(dealer), 'dealer')
        self.assertEqual(dealer.e_mail, 'dealer@gmail.com')


class TestCityModel(TestCase):
    def setUp(self) -> None:
        self.country = CountryFactory()

    def test_model(self):
        city = City.objects.create(
            name='Paris',
            country=self.country,
        )

        self.assertIsNotNone(city.id)
        self.assertEqual(str(city), 'Paris')


class TestCountryModel(TestCase):
    def test_model(self):
        country = Country.objects.create(
            name='Ukraine',
            code='380',
        )

        self.assertIsNotNone(country.id)
        self.assertEqual(str(country), 'Ukraine')
        self.assertEqual(country.code, '380')
