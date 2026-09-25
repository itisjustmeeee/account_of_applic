from models.statuses import Status
from models.services import (
    create_status,
    get_status_by_id,
    delete_status
)


def test_create_status():
    statuses = []

    status = create_status(
        statuses,
        1,
        'New'
    )

    assert isinstance(status, Status)
    assert status.id == 1
    assert status.name == 'New'


def test_rename_status():
    status = Status(1, 'New')

    status.rename('In progress')

    assert status.name == 'In progress'


def test_get_status_by_id():
    status = Status(1, 'New')
    statuses = [status]

    result = get_status_by_id(statuses, 1)

    assert result == status


def test_delete_status():
    status = Status(1, 'New')
    statuses = [status]

    result = delete_status(statuses, 1)

    assert result is True
    assert statuses == []
