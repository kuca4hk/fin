from django.urls import path
from .views import get_cars, get_cars_oldest, store_buy_car, store_selling_car, get_cars_most_expensive

urlpatterns = [
    path('cars/', get_cars, name='car-list'),
    path('oldest/', get_cars_oldest, name='car-list-oldest'),
    path('most-expensive/', get_cars_most_expensive, name='car-list-most-expensive'),
    path('store-buy-car/', store_buy_car, name='buy-car'),
    path('store-sell-car/<int:pk>/', store_selling_car, name='sell-car'),
]