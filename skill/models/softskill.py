from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class SoftSkill(models.Model):

    title = models.CharField(
        verbose_name='Soft Skill',
        max_length=40,
        blank=False,
        null=False
    )

    level = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(5)],
                                        default=0,
                                        verbose_name='Level')

    summary = models.TextField(
        max_length=600,
        null=True,
        blank=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
