import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


def test_user_has_patient_role_by_default():
    user = User(
        username="testuser",
        email="user@example.com",
    )

    assert user.role == User.Role.PATIENT


def test_username_field_is_email():
    assert User.USERNAME_FIELD == "email"


@pytest.mark.django_db
def test_create_user_saves_user_to_database():
    user = User.objects.create_user(
        username="testuser",
        email="user@example.com",
        password="StrongPassword123!",
    )

    saved_user = User.objects.get(email="user@example.com")

    assert user.pk is not None
    assert saved_user.email == "user@example.com"
    assert saved_user.username == "testuser"
    assert user.check_password("StrongPassword123!")


@pytest.mark.django_db
def test_rejects_duplicate_email():
    User.objects.create_user(
        username="firstuser",
        email="same@example.com",
        password="StrongPassword123!",
    )

    second_user = User(
        username="seconduser",
        email="same@example.com",
    )
    second_user.set_password("StrongPassword123!")

    with pytest.raises(ValidationError):
        second_user.full_clean()


def test_user_str_returns_email():
    user = User(
        username="testuser",
        email="user@example.com",
    )

    assert str(user) == "user@example.com"


@pytest.mark.django_db
def test_create_superuser_sets_staff_and_superuser_flags():
    admin_user = User.objects.create_superuser(
        username="adminuser",
        email="admin@example.com",
        password="StrongPassword123!",
    )

    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True
    assert admin_user.is_active is True
