from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = tuple(UserAdmin.fieldsets or ()) + (("Role", {"fields": ("role",)}),)
    add_fieldsets = tuple(UserAdmin.add_fieldsets or ()) + (
        ("Role", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")
    search_fields = ("email", "username")
    ordering = ("email",)
