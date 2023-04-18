# Generated by Django 3.2 on 2023-04-17 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('premiumplan', '0002_activeplan_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='createplan',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='register.user'),
            preserve_default=False,
        ),
    ]