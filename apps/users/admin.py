from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = (
        'username',
        'sex',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )
