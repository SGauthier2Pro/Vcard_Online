from django.db import models
from django.conf import settings

from .experience import Experience
from .hobbies import Hobbies
from .formation import Formation

from skill.models.technology import Technology
from skill.models.softskill import SoftSkill
from skill.models.language import Language


class Cv(models.Model):

    title = models.CharField(
        verbose_name='title',
        max_length=50,
        blank=False,
        null=False
    )

    profil = models.TextField(
        verbose_name='profil',
        max_length=600,
        blank=False,
        null=False,
        default='entrez une description de votre profil'
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    experiences = models.ManyToManyField(Experience, blank=True)

    softskills = models.ManyToManyField(SoftSkill, blank=True)

    languages = models.ManyToManyField(Language, blank=True)

    hobbies = models.ManyToManyField(Hobbies, blank=True)

    formations = models.ManyToManyField(Formation, blank=True)

    technologies = models.ManyToManyField(Technology, blank=True)

    can_be_display = models.BooleanField(
        verbose_name="can be display",
        default=False
    )

    def __str__(self):
        return self.title
