import abc


class UserCaseInterface(metaclass=abc.ABCMeta):
    # @abc.abstractmethod
    # def find_all():
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def delete(item):
    #     raise NotImplementedError

    @abc.abstractmethod
    def execute(item):
        raise NotImplementedError
