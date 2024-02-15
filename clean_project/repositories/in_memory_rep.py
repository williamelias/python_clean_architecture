import json
from clean_project import settings
from clean_project.entities.base_interface import EntityI
from clean_project.gateways.item_gw import GenericGateway
from pymemcache.client import base


class InMemoryRepository(GenericGateway):
    def __init__(self) -> None:

        # Don't forget to run `memcached' before running this next line:
        self.client = base.Client((settings.MEMORYCACHED_HOST, 11211))

    def create(self, entity: EntityI):
        # Once the client is instantiated, you can access the cache:
        self.client.set(entity.get_uuid(), json.dumps(entity.__dict__()))

        # Retrieve previously set data again:
        return self.client.get(entity.get_uuid())

    def update(entity: EntityI):
        return super().update()

    def get(entity: EntityI):
        return super().get()

    def delete(entity: EntityI):
        return super().delete()
