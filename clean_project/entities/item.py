from . import priority
from .exceptions import tem_exceptions
import uuid


class Item:
    def __init__(
        self, title: str, description: str, priority: priority.Priority
    ) -> None:
        self.__description = description
        self.__title = self.set_title(title=title)
        self.__priority = priority
        self.__checked = False
        self.__id = uuid.uuid4()

    def set_title(self, title: str):
        if len(title) < 3:
            raise tem_exceptions.TitleWithInvalidSizeException()
        return title

    def __str__(self) -> str:
        return self.get_title()

    def get_title(self):
        return self.__title

    def __lt__(self, other_item):
        """Override default '<' with new comparing
        embased in .priority field of objects

        Args:
            other_item (Item): _description_

        Returns:
            bool: if self priority is less than other.priority
        """
        return self.__priority.value < other_item.__priority.value

    def __gt__(self, other_item):
        """Override default '>' with new comparing
        embased in .priority field of objects

        Args:
            other_item (Item): _description_

        Returns:
            bool: if self priority is grethen than other.priority
        """
        return self.__priority.value > other_item.__priority.value

    def check(self):
        self.__checked = True

    def uncheck(self):
        self.__checked = False

    def get_description(self):
        return self.__description

    def update_description(self, new_description: str):
        self.__description = new_description

    def update_priority(self, new_priority: int):
        self.__priority = new_priority

    def get_priority(self):
        return self.__priority

    def get_id(self):
        return self.__id
