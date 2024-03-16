from django.contrib import admin
from .models import Store, TransactionLogSell, TransactionLogBuy

# Register your models here.

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionLogBuy)
class TransactionLogBuyAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionLogSell)
class TransactionLogSellAdmin(admin.ModelAdmin):
    pass

