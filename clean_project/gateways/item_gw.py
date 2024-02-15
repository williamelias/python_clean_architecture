import abc
from clean_project.entities.base_interface import EntityI


class GenericGateway(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(entity: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def update(entity: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def get(entity: EntityI):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(entity: EntityI):
        raise NotImplementedError
