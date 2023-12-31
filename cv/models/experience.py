from django.db import models
from django.conf import settings


class Experience(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=100,
        blank=False,
        null=False
    )

    company_name = models.CharField(
        verbose_name='Company name',
        max_length=100,
        blank=False,
        null=False
    )

    location = models.CharField(
        verbose_name='company location',
        max_length=100,
        blank=False,
        null=False
    )

    date_started = models.DateField(
        verbose_name='date started',
        null=False,
        blank=False
    )

    date_end = models.DateField(
        verbose_name='date end',
        blank=True,
        null=True
    )

    tasks = models.TextField(
        max_length=255,
        verbose_name='tasks',
        blank=True,
        null=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_started',)

    def __str__(self):
        return self.title
