from django.urls import path
from .views import get_cars, get_cars_oldest, buy_car, sell_car, get_cars_most_expensive

urlpatterns = [
    path('cars/', get_cars, name='car-list'),
    path('oldest/', get_cars_oldest, name='car-list-oldest'),
    path('most-expensive/', get_cars_most_expensive, name='car-list-most-expensive'),
    path('buy-car/<int:pk>/', buy_car, name='buy-car'),
    path('sell-car/', sell_car, name='sell-car'),
]