import uuid
from clean_project.entities.base_interface import EntityI


class Owner(EntityI):
    def __init__(self, name) -> None:
        self.__name = name
        self.__uuid = uuid.uuid4()

    def get_name(self):
        return self.__name

    def __str__(self) -> str:
        return self.get_name()

    def get_uuid(self):
        return self.__uuid.__str__()

    def __dict__(self):
        return {"uuid": self.get_uuid(), "name": self.get_name()}
