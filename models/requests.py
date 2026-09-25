from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .category import Category
    from .statuses import Status


class Request:
    def __init__(
        self,
        request_id: int,
        user: User,
        description: str,
        category: Category,
        status: Status,
        urgency: int
    ) -> None:
        self.id = request_id
        self.user = user
        self.description = description
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
            f'Описание: {self.description}\n'
            f'Ответ: {self.answer or 'Ответ отсутствует'}'
        )

    def change_status(self, status: Status) -> None:
        self.status = status

    def calculate_priority(self) -> str:
        if self.urgency == 1:
            return 'Высокий'
        elif self.urgency == 2:
            return 'Обычный'
        return 'Низкий'

    def add_answer(self, answer: str) -> None:
        self.answer = answer
