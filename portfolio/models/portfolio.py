"""
    model portfolio ne contenant que le text d'intro et la phrase de bienvenue mais devant servir
    à stocker les conf stylistique du portfolio
"""

from django.db import models
from django.conf import settings


class Portfolio(models.Model):

    title = models.CharField(
        verbose_name='title',
        max_length=60,
        blank=False,
        null=False
    )

    welcome_sentence = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Bienvenue !'
    )

    introduction_text = models.TextField(
        max_length=600,
        null=True,
        blank=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    is_visible = models.BooleanField(
        verbose_name="is visible",
        default=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

