# Generated by Django 4.2.5 on 2023-11-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_description_alter_project_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='can_be_display',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='can be display'),
        ),
    ]
