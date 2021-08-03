import factory


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'Porsche cars'
    email = 'porscheseller13@gmail.com'
    city_id = 4
    user_id = 1


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'United Kingdom'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'London'
    country_id = 6
