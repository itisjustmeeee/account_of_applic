from storage import load_data, save_data


def test_save_and_load(tmp_path):
    """Проверяет сохранение и загрузку данных."""

    filename = tmp_path / "test.json"

    data = [
        {
            "id": 1,
            "name": "Ivan"
        }
    ]

    save_data(str(filename), data)

    result = load_data(str(filename))

    assert result == data