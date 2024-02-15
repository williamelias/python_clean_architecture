from uuid import uuid4
from clean_project.entities.base_interface import EntityI


class CustomEntity(EntityI):
    def __init__(self) -> None:
        self.__uuid = uuid4()

    def get_uuid(self) -> str:
        return self.__uuid.__str__()

    def __dict__(self):
        return {"uuid": self.get_uuid(), "title": "custom title"}
