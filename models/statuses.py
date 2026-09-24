class Status:
    def __init__(
        self,
        status_id: int,
        name: str
    ) -> None:
        self.id = status_id
        self.name = name

    def __str__(self) -> str:
        return f'Статус #{self.id}: {self.name}'

    def rename(self, new_name: str) -> None:
        self.name = new_name


def create_status(
    statuses: list[Status],
    status_id: int,
    name: str
) -> Status:
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
