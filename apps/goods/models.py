from django.db import models


# Create your models here.
class Good(models.Model):
    """
    Model representing the information of commodity
    """
    product_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)
    game_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product_name
