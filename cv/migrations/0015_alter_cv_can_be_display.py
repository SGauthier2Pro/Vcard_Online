# Generated by Django 4.2.5 on 2023-11-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0014_alter_cv_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='can_be_display',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='can be display'),
        ),
    ]
