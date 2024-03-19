from rest_framework import generics
from .models import Car
from ..store.models import Store, TransactionLog
from .serializer import CarSerializer
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
import json


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_cars_most_expensive(request):
    cars = Car.objects.all().order_by('-price')[:10]
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_cars_oldest(request):
    cars = Car.objects.all().order_by('added_to_inventory')[:10]
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def store_selling_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
        deleted_car = {
            'model': car.model,
            'brand': car.brand,
            'price': str(car.price),
            'manufacturing_year': car.manufacturing_year,
        }
        TransactionLog.objects.create(
            user=request.user,
            action='sell',
            deleted_car=json.dumps(deleted_car),
            deleted_car_price=car.price
        )
        Store.objects.all().update(money=F('money') + car.price)
        car.delete()
        return Response('Car bought successfully')
    except Car.DoesNotExist:
        return Response('Car not found', status=404)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def store_buy_car(request):
    if Store.objects.first() is None:
        return Response('The Store doesnt exist', status=404)
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        if request.data['price'] - Store.objects.first().money > 0:
            return Response('Not enough money in the store', status=400)
        car = serializer.save()
        Store.objects.all().update(money=F('money') - car.price)
        TransactionLog.objects.create(car=car, user=request.user, action='buy')
        return Response(serializer.data, status=201)
    return Response(serializer.errors)
