from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street} {self.zip_code} {self.city} {self.country_iso_code}'

    class Meta:
        verbose_name_plural = "Addresses"


class CustomUser(AbstractUser):

    first_name = models.CharField(
        max_length=25,
        verbose_name='First name',
        blank=True
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name='Last name'
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email',
        unique=True
    )
    phone_number_regex = RegexValidator(
        regex='(0|\\+33|0033)[1-9][0-9]{8}'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone',
        blank=True,
        validators=[phone_number_regex]
    )
    mobile = models.CharField(
        max_length=20,
        verbose_name='Mobile',
        blank=True,
        validators=[phone_number_regex]
    )
    birth_date = models.DateField(
        blank=True,
        null=True
    )
    location = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    linkedin_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
