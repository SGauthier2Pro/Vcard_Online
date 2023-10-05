from django.db import models


class Cv(models.Model):

    title = models.CharField(
        verbose_name='title',
        max_length=50,
        blank=False,
        null=False
    )

    background_personal_details_panel = models.ImageField(
        verbose_name='background left panel'

    )

    background_title_panel = models.ImageField(
        verbose_name='background title panel'

    )

    background_experience_title = models.ImageField(
        verbose_name='background job title',

    )

    background_education_title = models.ImageField(
        verbose_name='background grade title'

    )

    def __str__(self):
        return self.title
