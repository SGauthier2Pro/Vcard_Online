# Generated by Django 4.2.5 on 2023-10-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('background_personal_details_panel', models.ImageField(upload_to='', verbose_name='background left panel')),
                ('background_title_panel', models.ImageField(upload_to='', verbose_name='background title panel')),
                ('background_experience_title', models.ImageField(upload_to='', verbose_name='background job title')),
                ('background_education_title', models.ImageField(upload_to='', verbose_name='background grade title')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company name')),
                ('location', models.CharField(max_length=100, verbose_name='company location')),
                ('date_started', models.DateField(verbose_name='date started')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='date end')),
                ('tasks', models.TextField(blank=True, max_length=255, null=True, verbose_name='tasks')),
                ('cvs', models.ManyToManyField(to='cv.cv')),
            ],
        ),
    ]
