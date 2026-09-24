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


def create_category(
    categories: list[Category],
    category_id: int,
    name: str,
    description: str = ''
) -> Category:

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
