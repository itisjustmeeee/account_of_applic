
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .requests import Request
    from .category import Category
    from .statuses import Status


class Guest:
    def __init__(self, name: str = 'Гость') -> None:
        self.name = name

    def __str__(self) -> str:
        return f'Гость: {self.name}'

    def register_user(
        self,
        users: list[User],
        user_id: int,
        username: str,
        password: str
    ) -> User | None:
        for user in users:
            if user.username == username:
                return None
        user = User(user_id, username, password)
        users.append(user)

        return user

    def login(
        self,
        users: list[User],
        username: str,
        password: str
    ) -> User | None:
        for user in users:
            if (
                user.username == username
                and user.password == password
            ):
                return user

        return None


class User:
    def __init__(
        self,
        user_id: int,
        username: str,
        password: str
    ) -> None:
        self.id = user_id
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f'Пользователь #{self.id}: {self.username}'

    def create_request(
        self,
        request_id: int,
        text: str,
        category: Category,
        status: Status,
        urgency: int
    ) -> Request:
        from .requests import Request
        return Request(
            request_id,
            self,
            text,
            category,
            status,
            urgency
        )

    def get_my_requests(
        self,
        requests: list[Request]
    ) -> list[Request]:
        return [
            request
            for request in requests
            if request.user.id == self.id
        ]

    def get_request(
        self,
        requests: list[Request],
        request_id: int
    ) -> Request | None:

        for request in requests:
            if (
                request.id == request_id
                and request.user.id == self.id
            ):
                return request

        return None


class Admin:
    def __init__(
        self,
        admin_id: int,
        username: str,
        password: str
    ) -> None:
        self.id = admin_id
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f'Админ #{self.id}: {self.username}'

    def change_request_status(
        self,
        request: Request,
        status: Status
    ) -> None:
        request.change_status(status)

    def answer_request(
        self,
        request: Request,
        answer: str
    ) -> None:
        request.add_answer(answer)

    def update_category(
        self,
        category: Category,
        new_name: str
    ) -> None:
        category.rename(new_name)

    def update_status(
        self,
        status: Status,
        new_name: str
    ) -> None:
        status.rename(new_name)
