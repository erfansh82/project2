# Generated by Django 3.2 on 2023-04-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20230413_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='winrate_crypto',
        ),
        migrations.RemoveField(
            model_name='user',
            name='winrate_forex',
        ),
    ]
