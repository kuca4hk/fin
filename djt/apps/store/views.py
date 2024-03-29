from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Car, Store, TransactionLog
from .serializer import StoreStatsSerializer, TransactionLogSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
# Create your views here.


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_store_stats(request):
    if request.user.is_superuser:
        store = Store.objects.first()
        serializer = StoreStatsSerializer(store, many=False)
        return Response(serializer.data)
    return Response('Unauthorized', status=401)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_store_logs(request):
    if request.user.is_superuser:
        trans_logs = TransactionLog.objects.all()
        serializer = TransactionLogSerializer(trans_logs, many=True)
        return Response(serializer.data)
    return Response('Unauthorized', status=401)
