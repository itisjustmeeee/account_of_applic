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
