# Generated by Django 4.2.5 on 2023-10-11 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0009_alter_formation_certificate_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbies',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]