# Generated by Django 4.2.5 on 2023-10-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_project_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='description'),
        ),
    ]
