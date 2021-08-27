from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.dealers.tests.factories import DealerFactory
from apps.cars.tests.factories import PictureFactory, ColorFactory, ModelFactory, PropertyFactory, FuelTypeFactory, BrandFactory
from apps.cars.models import Car, Picture, Color, Model, Brand, Property, FuelType


class TestCarModel(TestCase):
    def setUp(self) -> None:
        self.dealer = DealerFactory()
        self.picture = PictureFactory()
        self.color = ColorFactory()
        self.model = ModelFactory()
        self.property = PropertyFactory()
        self.fuel = FuelTypeFactory()

    def test_model(self):
        car = Car.objects.create(
            number='AB-12-CD',
            slug='12AB',
            engine_power=180,
            price=60000,
            capacity=2.0,
            dealer=self.dealer,
            picture=self.picture,
            color=self.color,
            model=self.model,
            fuel=self.fuel,
        )
        car.property.add(self.property)

        self.assertIsNotNone(car.id)
        self.assertEqual(str(car), '12AB')
        self.assertEqual(car.number, 'AB-12-CD')
        self.assertEqual(car.engine_power, 180)
        self.assertEqual(car.price, 60000)
        self.assertEqual(car.capacity, 2.0)
        self.assertEqual(car.doors, 4)
        self.assertEqual(car.sitting_place, 5)
        self.assertEqual(car.engine_type, Car.ENGINE_STRAIGHT)
        self.assertEqual(car.pollutant_type, Car.POLLUTANT_A)
        self.assertEqual(car.status, Car.STATUS_FOR_SALE)
        self.assertEqual(car.gear_case, Car.GEAR_MANUAL)


class TestPictureModel(TestCase):
    def test_model(self):
        picture = Picture.objects.create(
            position=10,
            metadata='some test metadata',
            url=SimpleUploadedFile(
                name='test.jpg',
                content=open('pictures/test.jpg', 'rb').read(),
                content_type='image/jpeg'
            )
        )

        self.assertIsNotNone(picture.id)
        self.assertIsNotNone(picture.url)
        self.assertEqual(picture.position, 10)
        self.assertEqual(picture.metadata, 'test metadata')


class TestColorModel(TestCase):
    def test_model(self):
        color = Color.objects.create(
            name='Black',
        )

        self.assertIsNotNone(color.id)
        self.assertEqual(str(color), 'Black')


class TestModelOfCarModel(TestCase):
    def setUp(self) -> None:
        self.brand = BrandFactory()

    def test_model(self):
        model = Model.objects.create(
            name='Carrera',
            brand=self.brand,
        )

        self.assertIsNotNone(model.id)
        self.assertEqual(str(model), 'Carrera')


class TestBrandModel(TestCase):
    def test_model(self):
        brand = Brand.objects.create(
            name='Porsche',
        )

        self.assertIsNotNone(brand.id)
        self.assertEqual(str(brand), 'Porsche')


class TestPropertyModel(TestCase):
    def test_model(self):
        property = Property.objects.create(
            name='test property name',
        )

        self.assertIsNotNone(property.id)
        self.assertEqual(str(property), 'test property name')
        self.assertEqual(property.category, Property.CATEGORY_MIDSIZE)


class TestFuelTypeModel(TestCase):
    def test_model(self):
        fuel = FuelType.objects.create()

        self.assertIsNotNone(fuel.id)
        self.assertEqual(str(fuel), FuelType.FUEL_PETROL)
