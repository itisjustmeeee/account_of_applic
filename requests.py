def calculate_priority(urgency: int) -> str:
    """Определяет приоритет заявки по уровню срочности."""

    if urgency == 3:
        return "Высокий"
    if urgency == 2:
        return "Обычный"
    return "Низкий"

def add_request(request):
    pass


def show_my_requests(requests):
    pass


def delete_request(request):
    pass


def change_status(request):
    pass


def answer_request(request):
    pass