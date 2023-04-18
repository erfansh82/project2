from django.contrib import admin

from .models import CreateSignal,ForexSignal,CryptoSignal


@admin.register(CreateSignal)
class CreateSignalAdmin(admin.ModelAdmin):
    list_display=('market_watch','live_price','signal_type','entry_price','take_profit','stop_loss',)
    search_fields=('market_watch','signal_type','live_price',)


@admin.register(ForexSignal)
class ForexSignalAdmin(admin.ModelAdmin):
    list_display=('user','forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('forex_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)


@admin.register(CryptoSignal)
class CryptoSignalAdmin(admin.ModelAdmin):
    list_display=('user','crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
    search_fields=('crypto_winrate','total_stop_loss','total_take_profit','total_stop_loss_pips','total_take_profit_pips','total_signal',)
