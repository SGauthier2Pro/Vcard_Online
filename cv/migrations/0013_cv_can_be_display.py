# Generated by Django 4.2.5 on 2023-10-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_alter_formation_rncp_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='can_be_display',
            field=models.BooleanField(default=False, verbose_name='can be display'),
        ),
    ]