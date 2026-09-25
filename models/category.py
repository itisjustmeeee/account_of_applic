class Category:

    def __init__(
        self,
        category_id: int,
        name: str,
        description: str = ""
    ) -> None:
        self.id = category_id
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f'Категория #{self.id}: {self.name}'

    def rename(self, new_name: str) -> None:
        self.name = new_name

    def update_description(
            self,
            new_description: str
    ) -> None:
        self.description = new_description
