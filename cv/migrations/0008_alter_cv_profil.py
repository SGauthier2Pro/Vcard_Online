# Generated by Django 4.2.5 on 2023-10-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_formation_certificate_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='profil',
            field=models.TextField(default='entrez une description de votre profil', max_length=255, verbose_name='profil'),
        ),
    ]