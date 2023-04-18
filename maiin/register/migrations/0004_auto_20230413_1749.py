# Generated by Django 3.2 on 2023-04-13 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createsignal', '0001_initial'),
        ('register', '0003_user_totalsignal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='totalsignal',
            new_name='total_signal_forex',
        ),
        migrations.AddField(
            model_name='user',
            name='total_signal_crypto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='createsignal.cryptosignal'),
            preserve_default=False,
        ),
    ]