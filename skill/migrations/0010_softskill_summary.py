# Generated by Django 4.2.5 on 2023-11-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0009_remove_language_cvs'),
    ]

    operations = [
        migrations.AddField(
            model_name='softskill',
            name='summary',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
