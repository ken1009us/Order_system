from django.db import models

from ..users.models import User
from ..goods.models import Good


class Order(models.Model):
    """
    Model representing the information of orders
    """
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    product_name = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        max_length=100,
        null=True,
        blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    delivery_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.username)
