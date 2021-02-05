from django.contrib import admin

from .models import Commodity


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'platform',
        'game_type',
        'price',
        'in_stock',
    )
