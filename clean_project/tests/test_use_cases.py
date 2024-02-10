from unittest import mock
import pytest
from entities.priority import Priority
from user_cases.item_us import CreateItemUS


@pytest.fixture()
def create_todo_gateway():
    gateway = mock.Mock()
    gateway.create = lambda x: x
    yield gateway


def test_create_item_us_must_return_valid_data(create_todo_gateway):
    item_data = {
        "title": "titulo",
        "description": "description",
        "priority": Priority.HIGHEST,
    }
    us = CreateItemUS(gateway=create_todo_gateway)
    output = us.execute(item_data)

    assert item_data == output
