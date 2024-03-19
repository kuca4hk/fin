from django.urls import path
from .views import get_store_stats, get_store_logs

urlpatterns = [
    path('store-log/', get_store_logs, name='get-store-logs'),
    path('store-stats/', get_store_stats, name='store-stats'),
]