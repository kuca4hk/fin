from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


    def create(self, validated_data):
        return Car.objects.create(**validated_data)


    def delete(self, instance):
        instance.delete()
        return instance