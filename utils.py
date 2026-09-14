import random


def generate_id() -> int:
    """Генерирует идентификатор заявки."""

    return random.randint(1000, 9999)

def is_valid_urgency(urgency: int) -> bool:
    """Проверяет корректность уровня срочности."""

    return 1 <= urgency <= 3