import factory
from factory import fuzzy

from apps.dealers.tests.factories import DealerFactory


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = factory.Sequence(lambda n: f'color_{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = factory.Sequence(lambda n: f'brand_{n}')


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = factory.Sequence(lambda n: f'property_{n}')


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Picture'

    position = fuzzy.FuzzyInteger(0, 100)
    metadata = fuzzy.FuzzyText(length=255)
    url = factory.django.ImageField(from_path='pictures/test.jpg')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    name = factory.Sequence(lambda n: f'model_{n}')
    brand = factory.SubFactory(BrandFactory)


class FuelTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.FuelType'


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'AB-12-CD'
    slug = factory.Sequence(lambda n: f'slug_{n}')
    engine_power = fuzzy.FuzzyInteger(50, 200)
    color = factory.SubFactory(ColorFactory)
    brand = factory.SubFactory(BrandFactory)
    property = factory.SubFactory(PropertyFactory)
    dealer = factory.SubFactory(DealerFactory)
    picture = factory.SubFactory(PictureFactory)
    model = factory.SubFactory(ModelFactory)
    fuel = factory.SubFactory(FuelTypeFactory)
