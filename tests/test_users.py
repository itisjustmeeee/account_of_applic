from models.users import login_user


def test_login_existing_user():
    """Проверяет вход существующего пользователя."""

    users = [
        {
            "name": "Ivan",
            "password": "1234",
            "role": "user"
        }
    ]

    result = login_user(users, "Ivan", "1234")

    assert result is not None