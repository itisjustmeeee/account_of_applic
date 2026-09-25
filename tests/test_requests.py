from models.users import User
from models.category import Category
from models.statuses import Status
from models.requests import Request
from models.services import delete_user_request


def test_get_my_requests():
    user = User(101, 'LoLz3217', '5767Kj')
    user_num = User(102, 'Anonimus13', '35Ks7Xz')

    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request_numm_one = user.create_request(
        1,
        'АААА. У меня не работает акк в Kiwi. Как войти, памагите!!!!',
        category,
        status,
        1
    )

    request_numm_two = user_num.create_request(
        2,
        'Извните, пожалуйста, я не могу вспомнить пароль от windows. Можете помочь с этим?',
        category,
        status,
        1
    )

    requests = [request_numm_one, request_numm_two]

    my_requests = user.get_my_requests(requests)

    assert len(my_requests) == 1
    assert my_requests[0] == request_numm_one


def test_get_my_request():
    user = User(101, 'LoLz3217', '5767Kj')

    category = Category(1, 'Жиза')
    status = Status(1, 'В работе')

    request = user.create_request(
        1,
        'Не могу найти свои носки уже 3 дня. Что можно с этим сделать???!!!',
        category,
        status,
        2
    )

    requests = [request]

    result = user.get_request(requests, 1)

    assert result == request


def test_get_my_request_not_found():
    user = User(101, 'LoLz3217', '5767Kj')

    result = user.get_request([], 100)

    assert result is None


def test_delete_user_request():
    user = User(101, 'LoLz3217', '5767Kj')

    category = Category(1, 'Игры')
    status = Status(1, 'Новая')

    request = user.create_request(
        1,
        'Я не могу пройти уровень в геншине',
        category,
        status,
        2
    )

    requests = [request]

    result = delete_user_request(
        requests,
        user,
        1
    )

    assert result is True
    assert requests == []


def test_user_cannot_delete_other_request():
    user = User(101, 'LoLz3217', '5767Kj')
    user_num = User(102, 'Anonimus13', '35Ks7Xz')

    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request_numm_one = user_num.create_request(
        1,
        'АААА. У меня не работает акк в Kiwi. Как войти, памагите!!!!',
        category,
        status,
        1
    )

    requests = [request_numm_one]

    result = delete_user_request(
        requests,
        user,
        1
    )

    assert result is False
    assert len(requests) == 1


def test_priority_high():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request = Request(
        1,
        user,
        'АААА, у меня не доступна винда',
        category,
        status,
        1
    )

    assert request.priority == 'Высокий'


def test_priority_normal():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request = Request(
        1,
        user,
        'АААА, у меня не доступна винда',
        category,
        status,
        2
    )

    assert request.priority == 'Обычный'


def test_priority_low():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request = Request(
        1,
        user,
        'АААА, у меня не доступна винда',
        category,
        status,
        3
    )

    assert request.priority == 'Низкий'


def test_change_request_status():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Доступ')
    old_status = Status(1, 'Новая')
    new_status = Status(2, 'В работе')

    request = Request(
        1,
        user,
        'Problems with hsr!!!!',
        category,
        old_status,
        2
    )

    request.change_status(new_status)

    assert request.status == new_status


def test_add_answer():
    user = User(101, 'LoLz3217', '5767Kj')
    category = Category(1, 'Доступ')
    status = Status(1, 'Новая')

    request = Request(
        1,
        user,
        'Problem with zzz',
        category,
        status,
        2
    )

    request.add_answer(
        'Попробуй поменять интернет соединение или перезагрузи комп')

    assert request.answer == 'Попробуй поменять интернет соединение или перезагрузи комп'
