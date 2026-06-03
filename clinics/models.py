from django.conf import settings
from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name="doctors",
    )
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Doctor profile"
        verbose_name_plural = "Doctor profiles"
        ordering = ["specialty", "user"]

    def __str__(self):
        return f"{self.user} — {self.specialty}"
