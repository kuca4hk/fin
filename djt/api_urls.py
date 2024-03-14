from rest_framework.routers import DefaultRouter
from django.urls import include, path, re_path

router = DefaultRouter()

urlpatterns = [
    # path("users/", include("djt.apps.users.urls")),
    path("cars/", include("djt.apps.cars.urls")),
    path("store/", include("djt.apps.store.urls")),
    path("", include(router.urls)),
]