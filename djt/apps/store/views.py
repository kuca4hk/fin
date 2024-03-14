from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Car, Store, TransactionLog
from .serializer import StoreStatsSerializer
# Create your views here.


class StoreStatsView(generics.RetrieveAPIView):
    serializer_class = StoreStatsSerializer

    def get_object(self):
        return Store.objects.first()
