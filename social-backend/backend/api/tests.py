from unittest.mock import patch

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from mixer.backend.django import mixer


def fixture_superuser_env_variables(env_var_name: str):
    if env_var_name == "DJANGO_SUPERUSER_USERNAME":
        return "admin"
    if env_var_name == "DJANGO_SUPERUSER_EMAIL":
        return "some.mail@mail.com"
    if env_var_name == "DJANGO_SUPERUSER_PASSWORD":
        return "S0m3P@ssw0rd"


@pytest.mark.django_db
@patch(
    "api.management.commands.initadmin.config",
    autospec=True,
    side_effect=fixture_superuser_env_variables,
)
def test_initadmin_command__default_case(config_mock):
    call_command("initadmin")

    assert config_mock.call_count == 3

    user_list = User.objects.all()
    assert len(user_list) == 1

    user = user_list[0]
    assert user.username == "admin"
    assert user.email == "some.mail@mail.com"
    assert user.is_superuser is True


@pytest.mark.django_db
@patch(
    "api.management.commands.initadmin.config",
    autospec=True,
    side_effect=fixture_superuser_env_variables,
)
def test_initadmin_command__admin_already_exists(config_mock):
    # Create admin user
    mixer.blend(
        User, email="another.email@mail.com", username="other_admin", is_superuser=True
    )

    call_command("initadmin")

    assert config_mock.call_count == 3

    user_list = User.objects.all()
    # User count didn't change since we already had one user in DB before running
    # initadmin command
    assert len(user_list) == 1

    user = user_list[0]
    assert user.username == "other_admin"
    assert user.email == "another.email@mail.com"
    assert user.is_superuser is True
