import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Kateryna'
    last_name = 'Supruniuk'
    email = 'kate@gmail.com'
    phone = '+390931234567'
    car_id = 145
