from django.urls import path
from .views import StoreStatsView

urlpatterns = [
    path('store-stats/', StoreStatsView.as_view(), name='store-stats'),
]