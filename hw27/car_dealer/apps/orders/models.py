from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Order(models.Model):
    STATUS_OPEN = 'open'
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_ON_HOLD = "on hold"
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_OPEN, "Open"),
        (STATUS_IN_PROGRESS, "In-Progress"),
        (STATUS_ON_HOLD, "On Hold"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_COMPLETED, "Completed")
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
    )
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
    phone = models.CharField(
        validators=[phoneNumberRegex],
        max_length=20,
    )
    message = models.TextField(
        blank=True,
    )

    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='orders',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'