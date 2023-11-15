from django.db import models
from django.conf import settings


class Hobbies(models.Model):

    title = models.CharField(
        verbose_name='title',
        max_length=100,
        blank=False,
        null=False
    )

    description = models.TextField(
        verbose_name='description',
        max_length=255,
        blank=False,
        null=False,
        default='entrez une descirption'
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
