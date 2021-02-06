from .serializers import GoodSerializer
from .models import Good

from rest_framework import viewsets


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
