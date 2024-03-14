from rest_framework import generics
from .models import Car
from ..store.models import Store, TransactionLog
from .serializer import CarSerializer
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_cars_most_expensive(request):
    cars = Car.objects.all().order_by('-price')[:10]
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_cars_oldest(request):
    cars = Car.objects.all().order_by('added_to_inventory')[:10]
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def buy_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
        Store.objects.all().update(money=F('money') + car.price)
        TransactionLog.objects.create(car=car, action='buy')
        car.delete()
        return Response('Car bought successfully')
    except Car.DoesNotExist:
        return Response('Car not found', status=404)


@api_view(['POST'])
def sell_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        car = serializer.save()
        Store.objects.all().update(money=F('money') - car.price)
        TransactionLog.objects.create(car=car, action='sell')
        return Response(serializer.data)
    return Response(serializer.errors)
