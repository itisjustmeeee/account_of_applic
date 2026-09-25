from models.category import Category
from models.services import (
    create_category,
    get_category_by_id,
    delete_category
)


def test_create_category():
    categories = []

    category = create_category(
        categories,
        1,
        'Техника',
        'Технические проблемы с компом или ноутом'
    )

    assert isinstance(category, Category)
    assert category.id == 1
    assert category.name == 'Техника'
    assert len(categories) == 1


def test_rename_category():
    category = Category(1, 'Техника')

    category.rename('Проблемы с прог. обеспечением')

    assert category.name == 'Проблемы с прог. обеспечением'


def test_get_category_by_id():
    category = Category(1, 'Техника')
    categories = [category]

    result = get_category_by_id(categories, 1)

    assert result == category


def test_delete_category():
    category = Category(1, 'Техника')
    categories = [category]

    result = delete_category(categories, 1)

    assert result is True
    assert categories == []
