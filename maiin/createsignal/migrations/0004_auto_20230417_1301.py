# Generated by Django 3.2 on 2023-04-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createsignal', '0003_auto_20230416_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createsignal',
            name='market_watch',
            field=models.CharField(choices=[('EURUSD', 0), ('EURCHF', 1), ('EURGBP', 2), ('EURJPY', 3), ('EURAUD', 4), ('EURNZD', 5), ('EURCAD', 6), ('USDJPY', 7), ('USDCAD', 8), ('USDCHF', 9), ('CADCHF', 10), ('CADJPY', 11), ('CHFJPY', 12), ('GBPJPY', 13), ('GBPCHF', 14), ('GBPUSD', 15), ('GBPNZD', 16), ('GBPAUD', 17), ('GBPCAD', 18), ('AUDUSD', 19), ('AUDCAD', 20), ('AUDCHF', 21), ('AUDJPY', 22), ('AUDNZD', 23), ('NZDUSD', 24), ('NZDCAD', 25), ('NZDCHF', 26), ('NZDJPY', 27), ('XAUUSD', 28)], max_length=20),
        ),
        migrations.AlterField(
            model_name='createsignal',
            name='signal_type',
            field=models.CharField(choices=[('sell', 1), ('buy', 2), ('sell limit', 3), ('sell stop', 4), ('buy limit', 5), ('buy stop', 6)], max_length=25),
        ),
    ]