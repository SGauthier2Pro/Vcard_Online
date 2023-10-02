from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .address import Address


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

    profile_photo = models.ImageField(
        verbose_name='photo de profil',
        default='default_profile.png'
    )

    def __str__(self):
        return self.username
