from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinLengthValidator
from django_countries.fields import CountryField

from PIL import Image

import random
import string
from datetime import datetime


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
    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)],
        blank=True,
        null=True,
        verbose_name='Street number'
    )
    street = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Street name'
    )
    city = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name='City'
    )
    state = models.CharField(
        max_length=2,
        validators=[MinLengthValidator(2)],
        blank=True,
        null=True,
        verbose_name='State'
    )
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)],
        blank=True,
        null=True,
        verbose_name='Zip code'
    )
    country = CountryField(
        blank_label="(select country)",
        blank=True,
        null=True,
        verbose_name='Country'
    )

    linkedin_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    git_url = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    profile_photo = models.ImageField(
        verbose_name='photo de profile',
        default='default_profile.png'
    )

    guest_access_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Guest Access Code'
    )

    guest_access_code_set_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Guest Access Code Set At'
    )

    def __str__(self):
        return self.username

    IMAGE_MAX_SIZE = (215, 215)

    def resize_image(self):
        profile_photo = Image.open(self.profile_photo)
        profile_photo.thumbnail(self.IMAGE_MAX_SIZE)
        profile_photo.save(self.profile_photo.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_photo:
            self.resize_image()

    def generate_guest_access_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.guest_access_code = code
        self.guest_access_code_set_at = datetime.now()

    def reset_guest_access_code(self):
        if self.guest_access_code_set_at:
            now = datetime.now()
            if (now - self.guest_access_code_set_at).days >= 7:
                self.guest_access_code = None
