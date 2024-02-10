import typing
from . import item
from .exceptions import tem_exceptions
from . import owner


class TodoList:
    def __init__(self, owner: owner.Owner) -> None:
        self.__owner = owner
        self.items: typing.Iterable[item.Item] = []

    def validate_existence_of(self, item):
        if self.find(item.get_title()):
            raise tem_exceptions.DuplicatedItemException()

    def find(self, title: str):
        titles = [item.get_title() for item in self.items]

        return title in titles

    def add(self, item: item.Item):
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
