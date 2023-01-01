from unittest.mock import patch

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


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
