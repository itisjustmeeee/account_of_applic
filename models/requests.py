from models import User
from models import Category
from models import Status


class Request:
    def __init__(
        self,
        request_id: int,
        user: User,
        text: str,
        category: Category,
        status: Status,
        urgency: int
    ) -> None:
        self.id = request_id
        self.user = user
        self.text = text
        self.category = category
        self.status = status
        self.urgency = urgency
        self.priority = self.calculate_priority()
        self.answer = ""

    def __str__(self) -> str:
        return (
            f'Заявка #{self.id}\n'
            f'Пользователь: {self.user.username}\n'
            f'Категория: {self.category.name}\n'
            f'Статус: {self.status.name}\n'
            f'Приоритет: {self.priority}'
            f'Описание: {self.text}\n'
            f'Ответ: {self.answer or 'Ответ отсутствует'}'
        )

    def change_status(self, status: Status) -> None:
        self.status = status

    def calculate_priority(self) -> str:
        if self.urgency == 3:
            return 'Высокий'
        elif self.urgency == 2:
            return 'Обычный'
        return 'Низкий'

    def add_answer(self, answer: str) -> None:
        self.answer = answer
