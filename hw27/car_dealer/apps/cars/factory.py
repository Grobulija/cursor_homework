import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    slug= '12AB'
    number = 'AB-12-CD'
    engine_power = 180
    dealer_id = 1
    picture_id = 4
    color_id = 3
    model_id = 2
    price = 50000


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Black'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'Porsche'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'Sedan'
