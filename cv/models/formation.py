from django.db import models
from django.conf import settings


RNCP_LVL = (
    ('CAP', '3'),
    ('BAC', '4'),
    ('BAC+2', '5'),
    ('LICENCE Niv.6', '6'),
    ('MASTER|MBA|Executive MAB Niv.7', '7'),
    ('DOCTORAT|DBA|PhD Niv.8', '8')
)


class Formation(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=100,
        blank=False,
        null=False
    )

    school_name = models.CharField(
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

    rncp_level = models.CharField(
        verbose_name='RNCP Level',
        max_length=30,
        choices=RNCP_LVL,
        default='4',
        blank=True
    )

    certificate_picture = models.ImageField(
        verbose_name='Certificate picture',
        blank=True,
        null=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
