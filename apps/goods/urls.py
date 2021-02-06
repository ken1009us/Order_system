from django.urls import include, path

from rest_framework import routers

from .views import GoodViewSet


router = routers.SimpleRouter()
router.register('goods', GoodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
