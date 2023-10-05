from django.db import models
from cv.models.cv import Cv


LEVEL = (
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2')
)


class Language(models.Model):

    title = models.CharField(
        verbose_name='language',
        max_length=40,
        blank=False,
        null=False
    )

    level = models.CharField(
        verbose_name='level',
        max_length=2,
        choices=LEVEL,
        default='A1'
    )

    cvs = models.ManyToManyField(Cv)

    def __str__(self):
        return self.title
