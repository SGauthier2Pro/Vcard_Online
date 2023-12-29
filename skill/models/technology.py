from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image


class Technology(models.Model):
    title = models.CharField(
        verbose_name='technology',
        max_length=40,
        blank=False,
        null=False
    )

    level = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(5)],
                                        default=0,
                                        verbose_name='Level')

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    image = models.ImageField(null=True,
                              blank=True,
                              verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Technologies'

    IMAGE_MAX_SIZE = (215, 310)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()