from django.contrib import admin


from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'product_name',
        'quantity',
        'payment_method',
        'delivery_address',
    )
