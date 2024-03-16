from django.urls import path
from .views import get_store_stats, get_store_logs_buy, get_store_logs_sell

urlpatterns = [
    path('store-log-buy/', get_store_logs_buy, name='store-log-buy'),
    path('store-stats/', get_store_stats, name='store-stats'),
    path('store-log-sell/', get_store_logs_sell, name='store-log-sell'),
]