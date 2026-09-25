
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .category import Category
    from .statuses import Status
    from .requests import Request


def create_category(
    categories: list[Category],
    category_id: int,
    name: str,
    description: str = ''
) -> Category:
    from .category import Category

    category = Category(
        category_id,
        name,
        description
    )

    categories.append(category)
    return category


def get_all_categories(
    categories: list[Category]
) -> list[Category]:

    return categories


def get_category_by_id(
    categories: list[Category],
    category_id: int
) -> Category | None:

    for category in categories:
        if category.id == category_id:
            return category

    return None


def delete_category(
    categories: list[Category],
    category_id: int
) -> bool:

    for category in categories:
        if category.id == category_id:
            categories.remove(category)
            return True

    return False


def create_status(
    statuses: list[Status],
    status_id: int,
    name: str
) -> Status:
    from .statuses import Status

    status = Status(status_id, name)
    statuses.append(status)
    return status


def get_all_statuses(
    statuses: list[Status]
) -> list[Status]:
    return statuses


def get_status_by_id(
    statuses: list[Status],
    status_id: int
) -> Status | None:

    for status in statuses:
        if status.id == status_id:
            return status

    return None


def delete_status(
    statuses: list[Status],
    status_id: int
) -> bool:

    for status in statuses:
        if status.id == status_id:
            statuses.remove(status)
            return True

    return False


def delete_user_request(
    requests: list[Request],
    user: User,
    request_id: int
) -> bool:

    for request in requests:
        if (
            request.id == request_id
            and request.user.id == user.id
        ):
            requests.remove(request)
            return True

    return False


def get_all_requests(
    requests: list[Request]
) -> list[Request]:

    return requests


def delete_request(
    requests: list[Request],
    request_id: int
) -> bool:

    for request in requests:
        if request.id == request_id:
            requests.remove(request)
            return True

    return False


def get_all_users(
    users: list[User]
) -> list[User]:

    return users
