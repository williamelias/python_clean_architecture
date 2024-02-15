import pytest
import pymongo
from clean_project import settings
from clean_project.repositories.mongo_repository import MongoRepository
from clean_project.tests.repositories.utils import CustomEntity


@pytest.fixture
def custom_entity():
    yield CustomEntity()


@pytest.mark.usefixtures("custom_entity")
def test_creating_flow_with_mongo_server(custom_entity):
    repository = MongoRepository()
    document = repository.create(entity=custom_entity)
    document.pop('_id')
    assert document == custom_entity.__dict__()
