# Generated by Django 3.2 on 2023-04-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
    ]
