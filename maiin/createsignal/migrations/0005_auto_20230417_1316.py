# Generated by Django 3.2 on 2023-04-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createsignal', '0004_auto_20230417_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createsignal',
            name='market_watch',
            field=models.CharField(choices=[('EURUSD', 'EURUSD'), ('EURCHF', 'EURCHF'), ('EURGBP', 'EURGBP'), ('EURJPY', 'EURJPY'), ('EURAUD', 'EURAUD'), ('EURNZD', 'EURNZD'), ('EURCAD', 'EURCAD'), ('USDJPY', 'USDJPY'), ('USDCAD', 'USDCAD'), ('USDCHF', 'USDCHF'), ('CADCHF', 'CADCHF'), ('CADJPY', 'CADJPY'), ('CHFJPY', 'CHFJPY'), ('GBPJPY', 'GBPJPY'), ('GBPCHF', 'GBPCHF'), ('GBPUSD', 'GBPUSD'), ('GBPNZD', 'GBPNZD'), ('GBPAUD', 'GBPAUD'), ('GBPCAD', 'GBPCAD'), ('AUDUSD', 'AUDUSD'), ('AUDCAD', 'AUDCAD'), ('AUDCHF', 'AUDCHF'), ('AUDJPY', 'AUDJPY'), ('AUDNZD', 'AUDNZD'), ('NZDUSD', 'NZDUSD'), ('NZDCAD', 'NZDCAD'), ('NZDCHF', 'NZDCHF'), ('NZDJPY', 'NZDJPY'), ('XAUUSD', 'XAUUSD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='createsignal',
            name='signal_type',
            field=models.CharField(choices=[('sell', 'sell'), ('buy', 'buy'), ('sell limit', 'sell limit'), ('sell stop', 'sell stop'), ('buy limit', 'buy limit'), ('buy stop', 'buy stop')], max_length=25),
        ),
    ]
