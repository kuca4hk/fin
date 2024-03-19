from rest_framework import serializers
from .models import Car, Store, TransactionLog
from django.db.models import Sum


class StoreStatsSerializer(serializers.Serializer):
    total_cars_bought = serializers.SerializerMethodField()
    total_cars_sold = serializers.SerializerMethodField()
    total_money_earned = serializers.SerializerMethodField()
    total_money_spent = serializers.SerializerMethodField()
    total_money_store = serializers.SerializerMethodField()

    def get_total_cars_bought(self, obj):
        return TransactionLog.objects.filter(action='buy').count()

    def get_total_cars_sold(self, obj):
        return TransactionLog.objects.filter(action='sell').count()

    def get_total_money_earned(self, obj):
        return TransactionLog.objects.filter(action='sell').aggregate(total=Sum('deleted_car_price'))['total'] or 0

    def get_total_money_spent(self, obj):
        return TransactionLog.objects.filter(action='buy').aggregate(total=Sum('car__price'))['total'] or 0

    def get_total_money_store(self, obj):
        return Store.objects.first().money


class TransactionLogSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(source='user.email')
    car = serializers.StringRelatedField()

    class Meta:
        model = TransactionLog
        fields = ('car', 'user', 'action', 'timestamp', 'deleted_car')

    def get_car(self, obj):
        return f'{obj.car.brand}-{obj.car.model}'


