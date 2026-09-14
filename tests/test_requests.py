from requests import calculate_priority


def test_high_priority():
    """Проверяет высокий приоритет."""

    assert calculate_priority(3) == "Высокий"


def test_normal_priority():
    """Проверяет обычный приоритет."""

    assert calculate_priority(2) == "Обычный"


def test_low_priority():
    """Проверяет низкий приоритет."""

    assert calculate_priority(1) == "Низкий"