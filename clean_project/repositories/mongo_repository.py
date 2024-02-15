import pymongo
from clean_project import settings
from clean_project.entities.base_interface import EntityI

from clean_project.gateways.item_gw import GenericGateway


class MongoRepository(GenericGateway):
    def __init__(self, db="default") -> None:
        self.client = pymongo.MongoClient(settings.MONGO_HOST)
        self.db = self.client[db]

    def create(self, entity: EntityI) -> dict:
        collection_name = entity.__class__.__name__

        data = entity.__dict__()

        collection = self.db[collection_name]
        collection.insert_one(data)

        return collection.find_one({"uuid": data.get("uuid")})

    def delete(entity: EntityI):
        return super().delete()

    def update(entity: EntityI):
        return super().update()

    def get(entity: EntityI):
        return super().get()
