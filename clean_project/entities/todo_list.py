import typing
import uuid
from clean_project.entities import todo_item,owner
from clean_project.entities.exceptions import item_exceptions
from clean_project.entities.base_interface import EntityI


class TodoList(EntityI):
    def __init__(self, owner: owner.Owner, title: str) -> None:
        self.__owner = owner
        self.__title = title
        self.items: typing.Iterable[todo_item.Item] = []
        self.__uuid = uuid.uuid4()

    def set_title(self, title: str):
        self.__title = title

    def get_title(self):
        return self.__title

    def validate_existence_of(self, item):
        if self.find(item.get_title()):
            raise item_exceptions.DuplicatedItemException()

    def find(self, title: str):
        titles = [item.get_title() for item in self.items]

        return title in titles

    def add(self, item: todo_item.Item):
        self.validate_existence_of(item=item)
        self.items.append(item)
        self.sort()

    def sort(self):
        self.items.sort()

    def get(self, idx):
        return self.items[idx]

    def get_owner(self):
        return self.__owner

    def __str__(self) -> str:
        return f"{len(self.items)} ownered by {self.get_owner()}"

    def check(self, idx):
        self.items[idx].check()

    def uncheck(self, idx):
        self.items[idx].uncheck()

    def get_uuid(self):
        return self.__uuid.__str__()

    def __dict__(self):
        return {
            "uuid": self.get_uuid(),
            "title": self.get_title(),
            "items": [item.__dict__ for item in self.items],
        }
