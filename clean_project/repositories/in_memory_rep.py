import json
from clean_project.entities.base_interface import EntityI
from clean_project.gateways.item_gw import GenericGateway
from pymemcache.client import base


class InMemoryRepository(GenericGateway):
    def __init__(self) -> None:

        # Don't forget to run `memcached' before running this next line:
        self.client = base.Client(("localhost", 11211))

    def create(self, item: EntityI):
        # Once the client is instantiated, you can access the cache:
        self.client.set(item.get_uuid(), json.dumps(item.__dict__()))

        # Retrieve previously set data again:
        return self.client.get(item.get_uuid())

    def update(item: EntityI):
        return super().update()

    def get(item: EntityI):
        return super().get()

    def delete(item: EntityI):
        return super().delete()
