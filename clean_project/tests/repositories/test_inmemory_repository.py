import json
from uuid import uuid4
import pytest
from clean_project.entities.base_interface import EntityI
from clean_project.repositories.in_memory_rep import InMemoryRepository


class CustomItem(EntityI):
    def __init__(self) -> None:
        self.__uuid = uuid4()

    def get_uuid(self) -> str:
        return self.__uuid.__str__()

    def __dict__(self):
        return {"uuid": self.get_uuid(), "title": "custom title"}


@pytest.fixture
def item():
    yield CustomItem()


@pytest.mark.usefixtures("item")
def test_in_memory_repository_creating_item(item):
    repo = InMemoryRepository()
    created = repo.create(item=item)

    assert json.loads(created) == item.__dict__()
