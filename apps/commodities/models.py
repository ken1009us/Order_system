from django.db import models


# Create your models here.
class Commodity(models.Model):
    """
    Model representing the information of commodity
    """
    product_name = models.CharField(max_length=100,
                                    default="The Legend of Zelda: Breath of the Wild",
                                    unique=True)
    price = models.PositiveIntegerField()
    in_stock = models.IntegerField()
    platform = models.SlugField(default='Nintendo Switch')
    game_type = models.CharField(max_length=100, default='ACT')

    def __str__(self):
        return self.product_name
