# Generated by Django 4.2.5 on 2023-10-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='technology')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('cvs', models.ManyToManyField(to='cv.cv')),
                ('projects', models.ManyToManyField(to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Soft Skill')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('cvs', models.ManyToManyField(to='cv.cv')),
                ('projects', models.ManyToManyField(to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='language')),
                ('level', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], default='A1', max_length=2, verbose_name='level')),
                ('cvs', models.ManyToManyField(to='cv.cv')),
            ],
        ),
    ]
