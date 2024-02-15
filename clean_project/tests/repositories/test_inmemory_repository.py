import json
import pytest
from clean_project.repositories.in_memory_rep import InMemoryRepository
from clean_project.tests.repositories.utils import CustomEntity


@pytest.fixture
def custom_entity():
    yield CustomEntity()


@pytest.mark.usefixtures("custom_entity")
def test_in_memory_repository_creating_some_entity(custom_entity):
    repo = InMemoryRepository()
    created = repo.create(entity=custom_entity)

    assert json.loads(created) == custom_entity.__dict__()
