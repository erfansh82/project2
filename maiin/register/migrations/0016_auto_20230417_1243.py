# Generated by Django 3.2 on 2023-04-17 08:13

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_alter_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
