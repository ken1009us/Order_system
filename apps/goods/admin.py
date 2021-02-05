from django.contrib import admin

from .models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'platform',
        'game_type',
        'price',
        'in_stock',
    )
