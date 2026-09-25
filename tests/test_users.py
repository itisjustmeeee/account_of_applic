from models.users import User
from models.category import Category
from models.statuses import Status
from models.requests import Request


def test_create_user():
    user = User(101, 'LoLz3217', '5767Kj')

    assert user.id == 101
    assert user.username == 'LoLz3217'
    assert user.password == '5767Kj'


def test_user_str():
    user = User(101, 'LoLz3217', '5767Kj')

    assert str(user) == 'Пользователь #101: LoLz3217'


def test_create_request():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Тех. проблемы'),
    status = Status(1, 'Новая')

    request = user.create_request(
        1,
        'У меня не работает принтер. Все черное!!! Что делааать???',
        category,
        status,
        3
    )

    assert isinstance(request, Request)
    assert request.id == 1
    assert request.user == user
    assert request.description == 'У меня не работает принтер. Все черное!!! Что делааать???'
    assert request.category == category
    assert request.status == status
    assert request.urgency == 3
