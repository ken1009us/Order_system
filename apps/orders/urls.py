from django.urls import include, path

from rest_framework import routers

from .views import OrderViewSet


router = routers.SimpleRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
