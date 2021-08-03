from django.db import models


# Create your models here.


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    picture = models.ForeignKey(
        'cars.Picture',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    property = models.ManyToManyField(
        'cars.Property',
    )
    fuel = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    ENGINE_STRAIGHT = 'straight'
    ENGINE_INLINE = 'inline'
    ENGINE_V = 'v'
    ENGINE_FLAT = 'flat'

    ENGINE_CHOICES = (
        (ENGINE_STRAIGHT, "Straight engine"),
        (ENGINE_INLINE, "Inline engine"),
        (ENGINE_V, "V engine"),
        (ENGINE_FLAT, "Flat engine")
    )

    POLLUTANT_A = 'a'
    POLLUTANT_B = 'b'
    POLLUTANT_C = 'c'
    POLLUTANT_D = 'd'
    POLLUTANT_E = 'e'
    POLLUTANT_F = 'f'
    POLLUTANT_G = 'g'

    POLLUTANT_CHOICES = (
        (POLLUTANT_A, "A"),
        (POLLUTANT_B, "B"),
        (POLLUTANT_C, "C"),
        (POLLUTANT_D, "D"),
        (POLLUTANT_E, "E"),
        (POLLUTANT_F, "F"),
        (POLLUTANT_G, "G")
    )

    STATUS_FOR_SALE = 'for sale'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_FOR_SALE, "For sale"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived")
    )

    GEAR_MANUAL = 'manual'
    GEAR_AUTOMATIC = 'automatic'
    GEAR_VARIABLE = 'variable'
    GEAR_SEMI_AUTOMATIC = 'semi-automatic'

    GEAR_CHOICES = (
        (GEAR_MANUAL, "Manual"),
        (GEAR_AUTOMATIC, "Automatic"),
        (GEAR_VARIABLE, "Variable"),
        (GEAR_SEMI_AUTOMATIC, "Semi-automatic")
    )

    engine_type = models.CharField(
        max_length=30,
        choices=ENGINE_CHOICES,
        default=ENGINE_STRAIGHT,
    )
    pollutant_class = models.CharField(
        max_length=5,
        choices=POLLUTANT_CHOICES,
        default=POLLUTANT_A,
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=30000
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_FOR_SALE,
    )
    doors = models.PositiveSmallIntegerField(
        default=4,
    )
    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=2.0
    )
    gear_case = models.CharField(
        max_length=20,
        choices=GEAR_CHOICES,
        default=GEAR_MANUAL,
    )
    number = models.CharField(
        max_length=15,
    )
    slug = models.SlugField(
        max_length=60,
    )
    sitting_place = models.PositiveSmallIntegerField(
        default=5,
    )
    first_registration_date = models.DateTimeField(
        auto_now_add=True,
    )
    engine_power = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Color(models.Model):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Model(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
        verbose_name='models',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Picture(models.Model):
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True,
    )
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Property(models.Model):
    CATEGORY_PASSENGER = 'passenger'
    CATEGORY_TRUCK = 'truck'
    CATEGORY_SPECIAL = 'special'


    CATEGORY_CHOICES = (
        (CATEGORY_PASSENGER, "Passenger"),
        (CATEGORY_TRUCK, "Truck"),
        (CATEGORY_SPECIAL, "Special")
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_PASSENGER
    )
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class FuelType(models.Model):
    FUEL_PETROL = 'petrol'
    FUEL_DIESEL = 'diesel'
    FUEL_ELECTRIC = 'electric'
    FUEL_GASOLINE = 'gasoline'

    FUEL_CHOICES = (
        (FUEL_PETROL, "Petrol"),
        (FUEL_DIESEL, "Diesel"),
        (FUEL_ELECTRIC, "Electric"),
        (FUEL_GASOLINE, "Gasoline")
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        default=FUEL_PETROL,
        unique=True,
    )

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = 'Fuel Type'
        verbose_name_plural = 'Fuel Types'
