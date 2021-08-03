from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(
        max_length=200,
    )
    e_mail = models.EmailField(
        max_length=80,
    )

    user = models.OneToOneField(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
        related_name='dealers',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class City(models.Model):
    name = models.CharField(
        max_length=100,
    )

    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='cities',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
