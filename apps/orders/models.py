from django.db import models

from ..users.models import User
from ..goods.models import Good


class Order(models.Model):
    """
    Model representing the information of orders
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Good, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=100, default="Credit card")
    delivery_address = models.CharField(max_length=100)
