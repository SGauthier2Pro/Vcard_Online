# Generated by Django 4.2.5 on 2023-10-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0008_remove_softskill_cvs_remove_softskill_projects_and_more'),
        ('project', '0003_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='softskills',
            field=models.ManyToManyField(to='skill.softskill'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='skill.technology'),
        ),
    ]
