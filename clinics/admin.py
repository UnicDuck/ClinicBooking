from django.contrib import admin

from .models import DoctorProfile, Specialty


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "specialty", "experience_years", "price")
    list_filter = ("specialty",)
    search_fields = ("user__email", "user__username", "specialty__name")
