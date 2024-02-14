import abc
from clean_project.entities.base_interface import EntityI


class GenericGateway(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(item: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def update(item: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def get(item: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(item: EntityI):
        raise NotImplementedError
