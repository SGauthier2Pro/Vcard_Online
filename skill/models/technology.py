from django.db import models
from django.conf import settings
from project.models.project import Project
from cv.models.cv import Cv
from django.core.validators import MinValueValidator, MaxValueValidator


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

    projects = models.ManyToManyField(
        Project
    )

    cvs = models.ManyToManyField(
        Cv
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Technologies'
