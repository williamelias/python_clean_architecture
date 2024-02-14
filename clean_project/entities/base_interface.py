import abc


class EntityI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_uuid(cls) -> str:
        raise NotImplementedError
