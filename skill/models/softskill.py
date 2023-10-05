from django.db import models
from project.models.project import Project
from cv.models.cv import Cv


class SoftSkill(models.Model):

    title = models.CharField(
        verbose_name='Soft Skill',
        max_length=40,
        blank=False,
        null=False
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    projects = models.ManyToManyField(
        Project
    )

    cvs = models.ManyToManyField(Cv)

    def __str__(self):
        return self.title
