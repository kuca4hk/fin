from rest_framework import serializers
from .models import Car, Store, TransactionLog
from django.db.models import Sum


class StoreStatsSerializer(serializers.Serializer):
    total_cars_bought = serializers.SerializerMethodField()
    total_cars_sold = serializers.SerializerMethodField()
    total_money_earned = serializers.SerializerMethodField()

    def get_total_cars_bought(self, obj):
        return TransactionLog.objects.filter(action='buy').count()

    def get_total_cars_sold(self, obj):
        return TransactionLog.objects.filter(action='sell').count()

    def get_total_money_earned(self, obj):
        return TransactionLog.objects.filter(action='sell').aggregate(total=Sum('car__price'))['total'] or 0
