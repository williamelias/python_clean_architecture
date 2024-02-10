import abc
from clean_project.entities.item import Item


class ItemGateway(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(item: Item):
        raise NotImplementedError
