from django.db import models
from django.conf import settings
from PIL import Image

from skill.models.technology import Technology
from skill.models.softskill import SoftSkill


class Project(models.Model):

    title = models.CharField(
        verbose_name='title',
        max_length=60,
        blank=False,
        null=False
    )

    description = models.TextField(
        verbose_name='description',
        max_length=255,
        blank=True,
        null=True
    )

    date_started = models.DateField(
        verbose_name='date started',
        null=False,
        blank=False
    )

    date_end = models.DateField(
        verbose_name='date end',
        auto_now=False,
        blank=True,
        null=True
    )

    technologies = models.ManyToManyField(Technology, blank=True)

    softskills = models.ManyToManyField(SoftSkill, blank=True)

    tasks = models.TextField(
        max_length=600,
        verbose_name='tasks',
        blank=True,
        null=True
    )

    link_git = models.URLField(
        verbose_name='link git',
        blank=True,
        null=True
    )

    presentation_file = models.FileField(
        verbose_name='Presentation file',
        blank=True,
        null=True
    )

    documents = models.FileField(
        verbose_name='Documents',
        blank=True,
        null=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)

    image = models.ImageField(null=True,
                              blank=True,
                              verbose_name='Image')

    can_be_display = models.BooleanField(
        verbose_name="can be display",
        default=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_task_list(self):
        if self.tasks:
            return str(self.tasks).split('-')
        else:
            return []

    IMAGE_MAX_SIZE = (215, 310)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()
