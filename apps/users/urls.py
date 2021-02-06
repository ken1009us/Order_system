from django.urls import include, path

from rest_framework import routers

from .views import UserViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
