from django.contrib import admin
from .models import Store, TransactionLog

# Register your models here.

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionLog)
class TransactionLogAdmin(admin.ModelAdmin):
    pass

