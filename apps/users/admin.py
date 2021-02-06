from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = (
        'username', 'sex', 'email', 'first_name', 'last_name', 'is_staff',
    )

    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal info', {'fields': ['first_name', 'last_name', 'sex']}),
        ('Permissions', {'fields': ['is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions']}),
        ('Important dates', {'fields': ['last_login', 'date_joined']}),
    ]
